from importlib import reload
from PySide6 import QtCore, QtWidgets
from NoraGeneral.UI import noraStringInputWidget
from NoraGeneral.noraUtilities import *

reload(noraStringInputWidget)

class NoraStringInput(QtWidgets.QDialog, noraStringInputWidget.Ui_noraStringInputLayoutDialog):
    def __init__(self, parent=None):
        super(NoraStringInput, self).__init__(parent)
        self.setParent(parent)
        self.setupUi(self)
        self.setLayout(self.StringInputLayout)

        self.text = ""
        self.lineEdit.textChanged.connect(self.value_changed)

    def value_changed(self):
        self.text = self.lineEdit.text()
