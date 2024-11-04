from importlib import reload
from PySide6 import QtCore, QtWidgets
from NoraGeneral.noraUtilities import *
from NoraUtilities.UI import noraJointSettingsWidget

reload(noraJointSettingsWidget)

def get_title():
    return 'Joint Settings'


def get_ui():
    return NoraJointSettings()


def get_width():
    return 460


def get_height():
    return 580


def get_use_custom_front_style():
    return False


class NoraJointSettings(QtWidgets.QDialog, noraJointSettingsWidget.Ui_noraJointSettingsWidget):
    def __init__(self, parent=None):
        super(NoraJointSettings, self).__init__(parent)
        self.setParent(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window)

        self.makeJointScaledUEStylePushButton.clicked.connect(self.make_selected_joint_scaled_ue_style)

    @staticmethod
    def make_selected_joint_scaled_ue_style():
        selected_objects = cmds.ls(selection=True, long=True, objectsOnly=True)
        for obj in selected_objects:
            object_type = cmds.objectType(obj)
            if object_type == 'joint':
                cmds.setAttr(f"{obj}.segmentScaleCompensate", True)
                parent = get_parent_joint(obj)
                if parent:
                    cmds.connectAttr(f"{parent}.scaleX", f"{obj}.scaleX", force=True)
                    cmds.connectAttr(f"{parent}.scaleY", f"{obj}.scaleY", force=True)
                    cmds.connectAttr(f"{parent}.scaleZ", f"{obj}.scaleZ", force=True)
