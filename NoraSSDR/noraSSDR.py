from importlib import reload
from PySide6 import QtCore, QtWidgets
from NoraSSDR.UI import noraSSDRWidget
from NoraGeneral import noraModelSelect
from NoraGeneral import noraMDagObjectSelect
from NoraGeneral import noraPathSelect
from NoraGeneral import noraFileList
from NoraGeneral import noraIntNumber

reload(noraSSDRWidget)
reload(noraModelSelect)
reload(noraMDagObjectSelect)
reload(noraPathSelect)
reload(noraFileList)
reload(noraIntNumber)


def get_title():
    return 'Method'


def get_ui():
    return NoraSSDR()


def get_width():
    return 460


def get_height():
    return 1000


def get_use_custom_front_style():
    return False


class NoraSSDR(QtWidgets.QDialog, noraSSDRWidget.Ui_noraSSDRWidget):
    def __init__(self, parent=None):
        super(NoraSSDR, self).__init__(parent)
        self.setParent(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window)

        # 添加ui
        self.target_model_widget = noraMDagObjectSelect.NoraMDagObjectSelect()
        self.target_model_widget.set_label_text("应用模型：")
        self.targetsVerticalLayout.addWidget(self.target_model_widget)

        self.joint_select_widget = noraMDagObjectSelect.NoraMDagObjectSelect()
        self.joint_select_widget.set_label_text("根关节：")
        self.targetsVerticalLayout.addWidget(self.joint_select_widget)

        self.rest_model_widget = noraPathSelect.NoraPathSelect()
        self.rest_model_widget.label.setText("绑定姿势：")
        self.targetsVerticalLayout.addWidget(self.rest_model_widget)

        self.anim_sequence_widget = noraPathSelect.NoraPathSelect()
        self.anim_sequence_widget.label.setText("关键帧序列：")
        self.targetsVerticalLayout.addWidget(self.anim_sequence_widget)

        self.label_sequence_widget = noraFileList.NoraFileList()
        self.label_sequence_widget.label.setText("标记序列：")
        self.targetsVerticalLayout.addWidget(self.label_sequence_widget)

        self.init_iter_num_widget = noraIntNumber.NoraIntNumber(8, 4, 128)
        self.init_iter_num_widget.label.setText("初始化迭代次数：")
        self.settingsVerticalLayout.addWidget(self.init_iter_num_widget)

        self.iter_num_widget = noraIntNumber.NoraIntNumber(16, 4, 128)
        self.iter_num_widget.label.setText("迭代次数: ")
        self.settingsVerticalLayout.addWidget(self.iter_num_widget)

        self.transform_iter_num_widget = noraIntNumber.NoraIntNumber(1, 1, 8)
        self.transform_iter_num_widget.label.setText("关节变换优化次数：")
        self.settingsVerticalLayout.addWidget(self.transform_iter_num_widget)

        self.weight_iter_num_widget = noraIntNumber.NoraIntNumber(1, 1, 8)
        self.weight_iter_num_widget.label.setText("权重优化次数")
        self.settingsVerticalLayout.addWidget(self.weight_iter_num_widget)

        self.max_influences_num_widget = noraIntNumber.NoraIntNumber(4, 1, 16)
        self.max_influences_num_widget.label.setText("顶点最大受影响关节数：")
        self.settingsVerticalLayout2.addWidget(self.max_influences_num_widget)

        self.max_joint_num_widget = noraIntNumber.NoraIntNumber(64, 1, 65535)
        self.max_joint_num_widget.label.setText("最大生成关节数：")
        self.settingsVerticalLayout2.addWidget(self.max_joint_num_widget)

