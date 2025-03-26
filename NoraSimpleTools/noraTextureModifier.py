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
    return NoraNormalMapping()


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


class NoraNormalMapping(QtWidgets.QDialog, noraTextureModifierWidget.Ui_noraTextureModifierWidget):
    def __init__(self):
        super(NoraNormalMapping, self).__init__()
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
                    new_image = NoraNormalMapping.remap_normal_tangent_mode(target_mesh, np_image, old_uv_set, new_uv_set, tol, f"{file_idx + 1}. {image_path}")
                else:
                    pass
            else:
                new_image = NoraNormalMapping.remap_uv(target_mesh, np_image, old_uv_set, new_uv_set, tol, f"{file_idx + 1}. {image_path}")
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
        triangle_nums = []
        triangle_indices = []
        triangle_maps = []
        for i in range(polygon_num):
            triangle_indices.append(in_mesh.getPolygonVertices(i))
            triangle_nums.append(len(triangle_indices[i]))
            # 构造一个顶点组合映射三角形的字典
            triangle_map = {}
            for j in range(triangle_nums[i] // 3):
                key_j = np.array([triangle_indices[i][j * 3], triangle_indices[i][j * 3 + 1], triangle_indices[i][j * 3 + 2]])
                sorted_key_j = NpArrayKey(np.sort(key_j, axis=None).reshape(key_j.shape))
                triangle_map[sorted_key_j] = j
            triangle_maps.append(triangle_map)

        progress_bar.start_progress_bar(status_text=bar_info, interruptable=False, max_value=image_shape[0])
        for i in range(image_shape[0]):
            progress_bar.set_progress_bar_value(i)
            for j in range(image_shape[1]):
                # 旧UV法线向量-模型空间-新UV法线向量
                normal = in_image[i, j, :]
                uv = rot_center + np.matmul(tex_to_uv_rot, np.array([i * step_i + half_step_i, j * step_j + half_step_j]) - rot_center)
                polygon_ids, points = in_mesh.getPointsAtUV(uv[0], uv[1], space=calcu_space, uvSet=in_old_uv, tolerance=in_tol)
                if points is not None:
                    for k in range(len(points)):
                        u, v, face_id = in_mesh.getUVAtPoint(points[k], space=calcu_space, uvSet=in_old_uv)
                        if face_id > 0:
                            # 计算出面上顶点的旧UV的切线和副切线，一个面一般有4个顶点
                            face_tangents = in_mesh.getFaceVertexTangents(face_id, space=calcu_space, uvSet=in_old_uv)
                            face_binormals = in_mesh.getFaceVertexBinormals(face_id, space=calcu_space, uvSet=in_old_uv)
                            # 获取face对应的顶点索引
                            face_vertex_num = len(face_tangents)
                            face_about_vertex_indices = []
                            for x in range(face_vertex_num):
                                face_vertex_info_idx = in_mesh.getFaceVertexIndex(face_id, x, localVertex=True) # uv 单独的顶点索引
                                print(face_vertex_info_idx)

                                ## 看起来，我最好还是自己找 Polygon 里的三角形，看哪个合适了，MFnMesh 这个 getFaceAndVertexIndices 会卡死

                                # face_about_vertex_indices.append(in_mesh.getFaceAndVertexIndices(face_vertex_info_idx, localVertex=False)[1]) # 映射出对应的顶点索引
                            # # 获取 face 包含的三角形
                            # polygon_id = polygon_ids[k]
                            # combinations = itertools.combinations(face_about_vertex_indices, 3)
                            # final_triangles = []
                            # for comb in combinations:
                            #     key_j = np.array([comb[0], comb[1], comb[2]])
                            #     sorted_key_j = NpArrayKey(np.sort(key_j, axis=None).reshape(key_j.shape))
                            #     if triangle_maps[polygon_id].__contains__(sorted_key_j):
                            #         final_triangles.append(triangle_maps[polygon_id][sorted_key_j])
                            # if len(final_triangles) != 0:
                            #     print(face_id, polygon_id)
                            #     break


        progress_bar.stop_progress_bar()
        return None
        return new_image