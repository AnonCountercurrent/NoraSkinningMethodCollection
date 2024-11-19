from importlib import reload
from PySide6 import QtCore, QtWidgets
from NoraGeneral.UI import noraPathSelectWidget
from NoraGeneral.noraUtilities import *

reload(noraPathSelectWidget)

class NoraPathSelect(QtWidgets.QDialog, noraPathSelectWidget.Ui_noraPathSelectDialog):
    def __init__(self, parent=None):
        super(NoraPathSelect, self).__init__(parent)
        self.setParent(parent)
        self.setupUi(self)
        self.setLayout(self.noraPathSelectHorizontalLayout)

        self.open_icon = self.style().standardIcon(getattr(QtWidgets.QStyle, "SP_DialogOpenButton"))
        self.pushButton.setIcon(self.open_icon)
        self.pushButton.clicked.connect(self.select_path)

    def get_path(self):
        return self.lineEdit.text()

    def select_path(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Path', get_document_path(), QtWidgets.QFileDialog.ShowDirsOnly)
        self.lineEdit.setText(path)