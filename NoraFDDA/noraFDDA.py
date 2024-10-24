from importlib import reload
from PySide2 import QtCore, QtWidgets
from NoraFDDA.UI import noraFDDAWidget
from NoraGeneral import noraModelSelect
from NoraGeneral import noraMDagObjectSelect

reload(noraFDDAWidget)
reload(noraModelSelect)
reload(noraMDagObjectSelect)


def get_title():
    return 'Method'


def get_ui():
    return NoraFDDA()


def get_width():
    return 460


def get_height():
    return 300


def get_use_custom_front_style():
    return False


class NoraFDDA(QtWidgets.QDialog, noraFDDAWidget.Ui_noraFDDAWidget):
    def __init__(self, parent=None):
        super(NoraFDDA, self).__init__(parent)
        self.setParent(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window)

        # 添加ui
        self.model_select_widget = noraModelSelect.NoraModelSelect()
        self.mdagSelectLayout.addWidget(self.model_select_widget)
        self.joint_select_widget = noraMDagObjectSelect.NoraMDagObjectSelect()
        self.joint_select_widget.set_label_text("根骨骼：")
        self.mdagSelectLayout2.addWidget(self.joint_select_widget)

        # 事件绑定
        self.bindVertexToJoint.clicked.connect(self.bind_vertex_to_joint)

    def bind_vertex_to_joint(self):
        pass
