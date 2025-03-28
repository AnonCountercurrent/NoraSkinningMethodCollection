from importlib import reload
from math import floor

from PySide6 import QtCore, QtWidgets
from NoraSimpleTools.UI import noraTextureModifierWidget
from NoraGeneral import noraUtilities, noraMDagObjectSelect, noraIntNumber, noraFileList, noraFloatNumber
reload(noraUtilities)
reload(noraTextureModifierWidget)
reload(noraUtilities)
reload(noraFileList)
reload(noraFloatNumber)
from NoraGeneral.noraUtilities import *
import maya.api.OpenMaya as om
import maya.cmds as cmds
from PIL import Image
import numpy as np
import itertools


def get_title():
    return 'Texture Modifier'


def get_ui():
    return NoraTextureModifier()


def get_width():
    return 460


def get_height():
    return 450


def get_use_custom_front_style():
    return False


class NpArrayKey:

    def __init__(self, array):
        self.array = np.array(array)

    def __hash__(self):
        return hash(self.array.tobytes())

    def __eq__(self, other):
        return np.array_equal(self.array, other.array)


class NoraTextureModifier(QtWidgets.QDialog, noraTextureModifierWidget.Ui_noraTextureModifierWidget):
    def __init__(self):
        super(NoraTextureModifier, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window)

        # uis
        self.origin_uv_index_widget = noraIntNumber.NoraIntNumber(min_value=0, max_value=8)
        self.origin_uv_index_widget.set_label_text("原始UV索引：")
        self.new_uv_index_widget = noraIntNumber.NoraIntNumber(min_value=0, max_value=8)
        self.new_uv_index_widget.set_label_text("新UV索引：")
        self.target_model_widget = noraMDagObjectSelect.NoraMDagObjectSelect()
        self.target_model_widget.set_label_text("目标网格体：")
        self.origin_tex_widget = noraFileList.NoraFileList()
        self.origin_tex_widget.set_label_text("原始纹理：")
        self.tol_widget = noraFloatNumber.NoraFloatNumber(default_value=0.0001, min_value=0.000001, max_value=0.1, decimals=6)
        self.tol_widget.set_label_text("精度：")

        self.texMapTargetslLayout.addWidget(self.target_model_widget)
        self.texMapTargetslLayout.addWidget(self.origin_tex_widget)
        self.texMapSettingslLayout.addWidget(self.origin_uv_index_widget)
        self.texMapSettingslLayout.addWidget(self.new_uv_index_widget)
        self.texMapSettingslLayout.addWidget(self.tol_widget)
        self.normal_check_box_changed()

        # events
        self.mappingPushButton.clicked.connect(self.mapping_texture)
        self.normalCheckBox.stateChanged.connect(self.normal_check_box_changed)

    def normal_check_box_changed(self):
        self.originTangentCheckBox.setEnabled(self.normalCheckBox.isChecked())

    def mapping_texture(self):
        # 获取参数
        is_normal_map = self.normalCheckBox.isChecked()
        origin_tangent_mode = self.originTangentCheckBox.isChecked()
        tol = self.tol_widget.number
        source_files = self.origin_tex_widget.get_file_list()
        origin_uv_index = self.origin_uv_index_widget.number
        new_uv_index = self.new_uv_index_widget.number
        if origin_uv_index == new_uv_index:
            print("原始UV索引不能等于新UV索引")
            return
        # 获取模型
        target_mesh = None # MFnMesh
        target_model_name = self.target_model_widget.get_dag_name()
        if cmds.objExists(target_model_name):
            cmds.select(target_model_name)
            target_mesh = om.MGlobal.getActiveSelectionList().getDagPath(0)
            target_mesh = om.MFnMesh(target_mesh)
            if target_mesh is None:
                print("\'目标网格体\' not set")
                return
            if target_mesh.numUVSets <= new_uv_index or target_mesh.numUVSets <= origin_uv_index:
                print("超出模型UV集数")
                return
        else:
            print("\'目标网格体\' not exists")
            return
        # 获取 UV　集
        uv_set_names = target_mesh.getUVSetNames()
        old_uv_set = uv_set_names[origin_uv_index]
        new_uv_set = uv_set_names[new_uv_index]
        print(f"{old_uv_set} to {new_uv_set}")
        # 循环处理
        progress_bar = NoraProgressBar()
        progress_bar.start_progress_bar(max_value=len(source_files))
        for file_idx in range(len(source_files)):
            progress_bar.set_progress_bar_value(file_idx)
            # 加载纹理
            image_path = source_files[file_idx]
            pil_image  = Image.open(image_path)
            if pil_image is None:
                print("图片 " + image_path + " 加载失败")
                continue
            np_image = np.array(pil_image)
            print(image_path)
            height, width, channels = np_image.shape
            print(f"Height: {height}, Width: {width}, Channels: {channels}")
            # 处理
            new_image = None
            if is_normal_map:
                if origin_tangent_mode:
                    new_image = NoraTextureModifier.remap_normal_tangent_mode(target_mesh, np_image, old_uv_set, new_uv_set, tol, f"{file_idx + 1}. {image_path}")
                else:
                    pass
            else:
                new_image = NoraTextureModifier.remap_uv(target_mesh, np_image, old_uv_set, new_uv_set, tol, f"{file_idx + 1}. {image_path}")
            if new_image is not None:
                img_to_save = Image.fromarray(new_image)
                suffix_pos = image_path.rfind('.')
                save_path = image_path[0:suffix_pos] + "New" + image_path[suffix_pos:len(image_path)]
                print("output: " + save_path)
                img_to_save.save(save_path)
            if progress_bar.is_progress_bar_cancelled():
                progress_bar.stop_progress_bar()
                return
        progress_bar.stop_progress_bar()

    @staticmethod
    def remap_uv(in_mesh:om.MFnMesh, in_image:np.ndarray, in_old_uv, in_new_uv, in_tol=0.0001, bar_info=""):
        calcu_space = om.MSpace.kObject
        new_image = np.zeros_like(in_image)
        image_shape = new_image.shape
        step_i = 1 / image_shape[0]
        step_j = 1 / image_shape[1]
        half_step_i = 0.5 * step_i
        half_step_j = 0.5 * step_j
        tex_to_uv_rot = np.array([[0, 1], [-1, 0]]) # uv左下角00，纹理左上角00，相当于逆时针旋转 90°
        uv_to_tex_rot = np.array([[0, -1], [1, 0]])
        rot_center = np.array([0.5, 0.5])
        progress_bar = NoraProgressBar()
        progress_bar.start_progress_bar(status_text=bar_info, interruptable=False, max_value=image_shape[0])
        for i in range(image_shape[0]):
            progress_bar.set_progress_bar_value(i)
            for j in range(image_shape[1]):
                # 纹理坐标 ij 映射到 uv 坐标
                new_uv = rot_center + np.matmul(tex_to_uv_rot, np.array([i * step_i + half_step_i, j * step_j + half_step_j]) - rot_center)
                # 新UV位置-模型坐标-旧UV位置
                polygon_ids, points = in_mesh.getPointsAtUV(new_uv[0], new_uv[1], space=calcu_space, uvSet=in_new_uv, tolerance=in_tol)
                if points is not None:
                    for k in range(len(points)):
                        old_u, old_v, face_id = in_mesh.getUVAtPoint(points[k], space=calcu_space, uvSet=in_old_uv)
                        # 将 uv 映射到纹理坐标
                        old_uv = rot_center + np.matmul(uv_to_tex_rot, np.array([old_u, old_v]) - rot_center)
                        # 找到新uv位置最近的像素点
                        new_image[i, j, :] = in_image[floor(old_uv[0] / step_i), floor(old_uv[1] / step_j), :]
                        break
        progress_bar.stop_progress_bar()
        return new_image

    @staticmethod
    def compute_tangent_basis(p1, p2, p3, uv1, uv2, uv3):
        edge1 = p2 - p1
        edge2 = p3 - p1
        edge1uv = (uv2[0] - uv1[0], uv2[1] - uv1[1])
        edge2uv = (uv3[0] - uv1[0], uv3[1] - uv1[1])
        cp = edge1uv[1] * edge2uv[0] - edge1uv[0] * edge2uv[1]
        if cp != 0.0:
            mul = 1.0 / cp
            tangent = (edge1 * -edge2uv[1] + edge2 * edge1uv[1]) * mul
            bitangent = (edge1 * -edge2uv[0] + edge2 * edge1uv[0]) * mul
            return tangent.normalize(), bitangent.normalize()
        return om.MVector(1, 0, 0), om.MVector(0, 1, 0)

    @staticmethod
    def compute_tnb_rot_matrix(p1, p2, p3, uv1, uv2, uv3):
        tnb_t, tnb_b = NoraTextureModifier.compute_tangent_basis(p1, p2, p3, uv1, uv2, uv3)
        tnb_n = (tnb_t ^ tnb_b).normalize()
        tnb_t = (tnb_t - (tnb_t * tnb_n) * tnb_n).normalize()
        tnb_b = (tnb_b - (tnb_b * tnb_n) * tnb_n - (tnb_b * tnb_t) * tnb_t).normalize()
        tnb_rot = np.array([[tnb_t.x, tnb_n.x, tnb_b.x],
                            [tnb_t.y, tnb_n.y, tnb_b.y],
                            [tnb_t.z, tnb_n.z, tnb_b.z]])
        return tnb_rot

    @staticmethod
    def point_triangle_distance(a, b, c, p):
        return 100

    @staticmethod
    def remap_normal_tangent_mode(in_mesh:om.MFnMesh, in_image:np.ndarray, in_old_uv, in_new_uv, in_tol=0.0001, bar_info=""):
        calcu_space = om.MSpace.kObject
        new_image = np.zeros_like(in_image)
        image_shape = new_image.shape
        step_i = 1 / image_shape[0]
        step_j = 1 / image_shape[1]
        half_step_i = 0.5 * step_i
        half_step_j = 0.5 * step_j
        tex_to_uv_rot = np.array([[0, 1], [-1, 0]])
        uv_to_tex_rot = np.array([[0, -1], [1, 0]])
        rot_center = np.array([0.5, 0.5])
        progress_bar = NoraProgressBar()
        # 收集好多边形和三角形
        polygon_num = in_mesh.numPolygons
        mesh_points = in_mesh.getPoints(space=calcu_space)
        mesh_triangle_info = in_mesh.getTriangles()

        progress_bar.start_progress_bar(status_text=bar_info, interruptable=False, max_value=image_shape[0])
        for i in range(image_shape[0]):
            progress_bar.set_progress_bar_value(i)
            for j in range(image_shape[1]):
                # 旧UV法线向量-模型空间-新UV法线向量
                normal = in_image[i, j, :] * 2 - 1
                uv = rot_center + np.matmul(tex_to_uv_rot, np.array([i * step_i + half_step_i, j * step_j + half_step_j]) - rot_center)
                polygon_ids, points = in_mesh.getPointsAtUV(uv[0], uv[1], space=calcu_space, uvSet=in_old_uv, tolerance=in_tol)
                if points is not None:
                    for k in range(len(points)):
                        goto_next_ij = False
                        point = om.MVector(points[k])
                        # 找到点属于的三角形
                        poly_idx = polygon_ids[k]
                        poly_tri_num = mesh_triangle_info[0][poly_idx]
                        for t in range(poly_tri_num):
                            t_idx1 = t * 3
                            t_idx2 = t * 3 + 1
                            t_idx3 = t * 3 + 2
                            p1 = om.MVector(mesh_points[mesh_triangle_info[1][poly_idx][t_idx1]])
                            p2 = om.MVector(mesh_points[mesh_triangle_info[1][poly_idx][t_idx2]])
                            p3 = om.MVector(mesh_points[mesh_triangle_info[1][poly_idx][t_idx3]])
                            if NoraTextureModifier.point_triangle_distance(p1, p2, p3, point) <= in_tol * 10:
                                uv1 = in_mesh.getPolygonUV(poly_idx, t_idx1, uvSet=in_old_uv)
                                uv2 = in_mesh.getPolygonUV(poly_idx, t_idx2, uvSet=in_old_uv)
                                uv3 = in_mesh.getPolygonUV(poly_idx, t_idx3, uvSet=in_old_uv)
                                tnb_mat = NoraTextureModifier.compute_tnb_rot_matrix(p1, p2, p3, uv1, uv2, uv3)
                                obj_space_normal = np.matmul(tnb_mat, normal[0:3])
                                new_uv1 = in_mesh.getPolygonUV(poly_idx, t_idx1, uvSet=in_old_uv)
                                new_uv2 = in_mesh.getPolygonUV(poly_idx, t_idx2, uvSet=in_old_uv)
                                new_uv3 = in_mesh.getPolygonUV(poly_idx, t_idx3, uvSet=in_old_uv)
                                new_tnb_mat = NoraTextureModifier.compute_tnb_rot_matrix(p1, p2, p3, new_uv1, new_uv2, new_uv3)
                                new_normal = np.matmul(np.transpose(new_tnb_mat), obj_space_normal)
                                new_normal = (new_normal + 1) * 0.5
                                new_image[i, j, 0:3] = new_normal
                                new_image[i, j, 3] = 1
                                goto_next_ij = True
                        if goto_next_ij:
                            break

        progress_bar.stop_progress_bar()
        return new_image