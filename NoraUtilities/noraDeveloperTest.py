from importlib import reload
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
        test_value_0 = self.doubleSpinBox.value()
        print(get_split_float_str(test_value_0))
