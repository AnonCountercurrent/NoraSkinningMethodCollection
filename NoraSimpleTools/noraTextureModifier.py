from importlib import reload
from PySide6 import QtCore, QtWidgets
from NoraSimpleTools.UI import noraTextureModifierWidget
from NoraGeneral import noraUtilities, noraMDagObjectSelect, noraIntNumber, noraFileList
reload(noraUtilities)
reload(noraTextureModifierWidget)
reload(noraUtilities)
reload(noraFileList)
from NoraGeneral.noraUtilities import *
import maya.api.OpenMaya as om
import maya.cmds as cmds


def get_title():
    return 'Texture Modifier'


def get_ui():
    return NoraNormalMapping()


def get_width():
    return 460


def get_height():
    return 600


def get_use_custom_front_style():
    return False


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

        self.originUVHorizontalLayout.addWidget(self.origin_uv_index_widget)
        self.targetUVHorizontalLayout.addWidget(self.new_uv_index_widget)
        self.targetModelHorizontalLayout.addWidget(self.target_model_widget)
        self.originTexHorizontalLayout.addWidget(self.origin_tex_widget)

        # events
        self.mappingPushButton.clicked.connect(self.mapping_texture)

    def mapping_texture(self):
        is_normal_map = self.normalCheckBox.isChecked()
        origin_tangent_mode = self.originTangentCheckBox.isChecked()
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
        else:
            print("\'目标网格体\' not exists")
            return

        # 处理纹理
        progress_bar = NoraProgressBar()
        progress_bar.start_progress_bar(len(source_files))
        for file_idx in range(len(source_files)):
            progress_bar.set_progress_bar_value(file_idx)
            # 加载纹理
            


        progress_bar.stop_progress_bar()

