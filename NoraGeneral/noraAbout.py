from importlib import reload
from PySide2 import QtCore, QtWidgets
from NoraGeneral.UI import noraAboutWidget
import webbrowser

reload(noraAboutWidget)


class NoraAbout(QtWidgets.QDialog, noraAboutWidget.Ui_noraAboutWidget):
    def __init__(self, parent=None):
        super(NoraAbout, self).__init__(parent)
        self.setParent(parent) # Parent
        self.setupUi(self) # setup
        self.setWindowFlags(QtCore.Qt.Window) # Flags [Qt.Tool, Qt.Widget, Qt.Window]
        self.link_str = ''
        self.linkButton.clicked.connect(self.goto_url)

    def set_text(self, in_text):
        self.label.setText(in_text)

    def set_link(self, in_link):
        self.link_str = in_link

    def goto_url(self):
        webbrowser.open(self.link_str)

