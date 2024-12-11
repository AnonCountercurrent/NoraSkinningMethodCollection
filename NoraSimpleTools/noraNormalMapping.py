from importlib import reload
from PySide6 import QtCore, QtWidgets
from NoraSimpleTools.UI import noraNormalMappingWidget
from NoraGeneral import noraUtilities
from NoraGeneral import noraMDagObjectSelect
reload(noraUtilities)
reload(noraNormalMappingWidget)
reload(noraUtilities)
from NoraGeneral.noraUtilities import *
import maya.api.OpenMaya as om
import maya.cmds as cmds


def get_title():
    return 'Normal Mapping'


def get_ui():
    return NoraNormalMapping()


def get_width():
    return 460


def get_height():
    return 600


def get_use_custom_front_style():
    return False


class NoraNormalMapping(QtWidgets.QDialog, noraNormalMappingWidget.Ui_noraNormalMappingWidget):
    def __init__(self):
        super(NoraNormalMapping, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window)

        # data
        self.selected_vertices = None

        # ui
        self.model_select_widget = noraMDagObjectSelect.NoraMDagObjectSelect()
        self.model_select_widget.set_label_text("操作目标网格：")
        self.meshDagPathSelectedLayout.addWidget(self.model_select_widget)
        self.curve_select_widget = noraMDagObjectSelect.NoraMDagObjectSelect()
        self.curve_select_widget.set_label_text("中心或曲线：")
        self.curveDagPathSelectedLayout.addWidget(self.curve_select_widget)
        self.shell_select_widget = noraMDagObjectSelect.NoraMDagObjectSelect()
        self.shell_select_widget.set_label_text("壳：")
        self.shellDagPathSelectedLayout.addWidget(self.shell_select_widget)

        # event
        self.cacheSelectedVerticesButton.clicked.connect(self.cache_selected_vertices)
        self.clearVertexCachePushButton.clicked.connect(self.clear_vertices_cache)
        self.normalMappingButton.clicked.connect(self.normal_mapping)

    def cache_selected_vertices(self):
        self.selected_vertices = cmds.ls(selection=True, flatten=True)
        self.vertexIndicesCountLineEdit.setText(str(len(self.selected_vertices)))

    def clear_vertices_cache(self):
        self.selected_vertices = None
        self.vertexIndicesCountLineEdit.setText("all")

    def normal_mapping(self):
        mapping_by_center = self.centerRadioButton.isChecked()
        mapping_by_curve = self.curveRadioButton.isChecked()
        mapping_by_distance = self.closestRadioButton.isChecked()
        two_way = self.twoWayCheckBox.isChecked()
        intersect_tol = self.tolSpinBox.value()
        center_curve_target = self.curve_select_widget.get_dag_name()
        shell_target_dag_path = self.shell_select_widget.get_dag_name()
        max_raidus = self.maxRadiusSpinBox.value()
        shell_mfn = None
        # curve/center
        if not mapping_by_distance:
            if cmds.objExists(center_curve_target):
                center_curve_target = noraUtilities.get_dag_path_by_name(center_curve_target)
                if mapping_by_curve:
                    center_curve_target = om.MFnNurbsCurve(center_curve_target)
                    if center_curve_target is None:
                        print("\'Center/Curve\' not a curve")
                        return
            else:
                print("\'Center/Curve\' not set")
                return
        # shell
        if cmds.objExists(shell_target_dag_path):
            shell_target_dag_path = noraUtilities.get_dag_path_by_name(shell_target_dag_path)
            mesh_node = noraUtilities.get_connect_object(shell_target_dag_path, om.MFn.kMesh)
            surface_node = noraUtilities.get_connect_object(shell_target_dag_path, om.MFn.kNurbsSurface)
            if mesh_node is not None:
                shell_mfn = om.MFnMesh(shell_target_dag_path)
                print("Shell is mesh")
            elif surface_node is not None:
                shell_mfn = om.MFnNurbsSurface(shell_target_dag_path)
                print("Shell is nurbs surface")
            else:
                print("\'Shell\' is not nurbs surface or mesh")
                return
        else:
            print("\'Shell\' not set")
            return
        # target
        target_mesh = None
        target_indices = []
        if self.selected_vertices is None:
            # all points on mesh
            target_model_name = self.model_select_widget.get_dag_name()
            if cmds.objExists(target_model_name):
                cmds.select(target_model_name)
                target_mesh = om.MGlobal.getActiveSelectionList().getDagPath(0)
                target_mesh = om.MFnMesh(target_mesh)
                if target_mesh is None:
                    print("\'Mesh\' not set")
                    return
                else:
                    target_indices = list(range(0, target_mesh.numVertices))
            else:
                print("\'Mesh\' not exists")
                return
        else:
            # split mesh idx from string array
            if len(self.selected_vertices) == 0:
                print("none cached vertices")
                return
            selected_vertices = cmds.filterExpand(self.selected_vertices, selectionMask=31, expand=True)
            if len(selected_vertices) == 0:
                return
            target_mesh = noraUtilities.get_dag_path_by_name(selected_vertices[0].split(".vtx")[0])
            target_mesh = om.MFnMesh(target_mesh)
            for i in range(len(selected_vertices)):
                idx = selected_vertices[i].split("[")[1].split("]")[0]
                target_indices.append(int(idx))

        process_bar = noraUtilities.NoraProgressBar()
        process_bar.start_progress_bar()
        vert_num = len(target_indices)
        process_bar_step = 100.0 / vert_num
        # intersect
        normal_list = []
        if mapping_by_center:
            vertices = target_mesh.getPoints(om.MSpace.kWorld)
            p1 = om.MTransformationMatrix(center_curve_target.inclusiveMatrix()).translation(om.MSpace.kWorld)
            p1_point = om.MPoint(p1)
            for i in range(vert_num):
                v_idx = target_indices[i]
                process_bar.set_progress_bar_value(process_bar_step * i)
                p2_point = vertices[v_idx]
                surface_normal = None
                if shell_mfn.type() == om.MFn.kMesh:
                    surface_normal = noraUtilities.get_intersect_normal_on_mesh_surface(shell_mfn, p1_point, p2_point, intersect_tol, two_way, max_raidus)
                else:
                    surface_normal = noraUtilities.get_intersect_normal_on_nurbs_surface(shell_mfn, p1_point, p2_point, intersect_tol, two_way, max_raidus)
                if surface_normal is None:
                    normal_list.append(target_mesh.getVertexNormal(v_idx, True, om.MSpace.kWorld))
                else:
                    normal_list.append(surface_normal)
        elif mapping_by_curve:
            vertices = target_mesh.getPoints(om.MSpace.kWorld)
            for i in range(vert_num):
                v_idx = target_indices[i]
                process_bar.set_progress_bar_value(process_bar_step * i)
                p2_point = vertices[v_idx]
                p1_point = center_curve_target.closestPoint(p2_point, tolerance=intersect_tol, space=om.MSpace.kWorld)[0]
                surface_normal = None
                if shell_mfn.type() == om.MFn.kMesh:
                    surface_normal = noraUtilities.get_intersect_normal_on_mesh_surface(shell_mfn, p1_point, p2_point, intersect_tol, two_way, max_raidus)
                else:
                    surface_normal = noraUtilities.get_intersect_normal_on_nurbs_surface(shell_mfn, p1_point, p2_point, intersect_tol, two_way, max_raidus)
                if surface_normal is None:
                    normal_list.append(target_mesh.getVertexNormal(v_idx, True, om.MSpace.kWorld))
                else:
                    normal_list.append(surface_normal)
        elif mapping_by_distance:
            vertices = target_mesh.getPoints(om.MSpace.kWorld)
            for i in range(vert_num):
                v_idx = target_indices[i]
                process_bar.set_progress_bar_value(process_bar_step * i)
                p2_point = vertices[v_idx]
                surface_normal = None
                if shell_mfn.type() == om.MFn.kMesh:
                    surface_normal = shell_mfn.getClosestNormal(p2_point, om.MSpace.kWorld)[0]
                else:
                    point_info = shell_mfn.closestPoint(p2_point)
                    surface_normal = shell_mfn.normal(point_info[1], point_info[2], om.MSpace.kWorld)
                if surface_normal is None:
                    normal_list.append(target_mesh.getVertexNormal(v_idx, True, om.MSpace.kWorld))
                else:
                    normal_list.append(surface_normal)

        target_mesh.setVertexNormals(normal_list, target_indices, om.MSpace.kWorld)
        process_bar.stop_progress_bar()

