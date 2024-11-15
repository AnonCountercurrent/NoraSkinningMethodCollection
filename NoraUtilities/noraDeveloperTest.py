from importlib import reload

import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from PySide6 import QtCore, QtWidgets
from NoraUtilities.UI import noraDeveloperTestWidget
from NoraGeneral import noraUtilities

reload(noraUtilities)
reload(noraDeveloperTestWidget)

from NoraGeneral.noraUtilities import *

def get_title():
    return 'Test'


def get_ui():
    return NoraDeveloperTest()


def get_width():
    return 460


def get_height():
    return 580


def get_use_custom_front_style():
    return False


class NoraDeveloperTest(QtWidgets.QDialog, noraDeveloperTestWidget.Ui_noraDeveloperTestWidget):
    def __init__(self, parent=None):
        super(NoraDeveloperTest, self).__init__(parent)
        self.setParent(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window)

        self.testPushButton.clicked.connect(self.test_button_clicked)

    def test_button_clicked(self):
        # test_value_0 = self.doubleSpinBox.value()
        # print(get_split_float_str(test_value_0))

        # X = np.arange(1, 8).reshape(1, 7)
        # poly = PolynomialFeatures(degree=2)
        # print(poly.fit_transform(X))
        bip001_joint = "Bip001"
        root_joint = "Root"
        bip001_dag = get_dag_path_by_name(bip001_joint)
        root_dag = get_dag_path_by_name(root_joint)
        oma.MAnimControl.setCurrentTime(om.MTime(0, om.MTime.k30FPS))
        rest_bip_ts = om.MFnTransform(bip001_dag)
        offset_vector = -rest_bip_ts.translation(om.MSpace.kWorld)
        cached_root_positions = []
        key_times = om.MTimeArray()
        channel_values = np.empty((18, 3), dtype=nora_scalar_type)
        for t in range(18):
            oma.MAnimControl.setCurrentTime(om.MTime(t, om.MTime.k30FPS))
            key_times.append(om.MTime(t, om.MTime.k30FPS))
            root_world_pos = om.MFnTransform(root_dag).translation(om.MSpace.kWorld) + offset_vector
            channel_values[t, 0] = root_world_pos.x
            channel_values[t, 1] = root_world_pos.y
            channel_values[t, 2] = root_world_pos.z

        set_keyframes(root_joint, "tx", key_times, channel_values[:, 0].tolist())
        set_keyframes(root_joint, "ty", key_times, channel_values[:, 1].tolist())
        set_keyframes(root_joint, "tz", key_times, channel_values[:, 2].tolist())




