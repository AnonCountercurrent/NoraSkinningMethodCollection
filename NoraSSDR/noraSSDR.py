from importlib import reload
from PySide6 import QtCore, QtWidgets
from NoraSSDR.UI import noraSSDRWidget
from NoraGeneral import noraModelSelect
from NoraGeneral import noraMDagObjectSelect

reload(noraSSDRWidget)
reload(noraModelSelect)
reload(noraMDagObjectSelect)


def get_title():
    return 'Method'


def get_ui():
    return NoraSSDR()


def get_width():
    return 460


def get_height():
    return 300


def get_use_custom_front_style():
    return False


class NoraSSDR(QtWidgets.QDialog, noraSSDRWidget.Ui_noraSSDRWidget):
    def __init__(self, parent=None):
        super(NoraSSDR, self).__init__(parent)
        self.setParent(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window)
        