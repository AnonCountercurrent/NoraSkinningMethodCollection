from importlib import reload
from PySide6 import QtCore, QtGui, QtWidgets
from NoraHelp.UI import noraHelpWidget
from NoraHelp.UI.noraHelpWidget import Ui_noraHelpWidget
from NoraGeneral.noraUtilities import *
import webbrowser

reload(noraHelpWidget)


def get_title():
    return 'About'


def get_ui():
    return NoraHelp()


def get_width():
    return 460


def get_height():
    return 500


def get_use_custom_front_style():
    return True


def create_by_link():
    webbrowser.open("https://github.com/AnonCountercurrent")


def docs_link():
    webbrowser.open("https://github.com/AnonCountercurrent/NoraSkinningMethodCollection")


class NoraHelp(QtWidgets.QDialog, Ui_noraHelpWidget):
    def __init__(self):
        super(NoraHelp, self).__init__()
        self.setParent(get_maya_main_window())
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window)
        self.gotoCreatedBy.clicked.connect(create_by_link)
        self.gotoDocs.clicked.connect(docs_link)

        self.picture = QtGui.QPixmap()
        self.picture.load(get_icon_path("Nora_Valkyrie_Emblem_128.png"))
        self.IconLabel.setPixmap(self.picture)

