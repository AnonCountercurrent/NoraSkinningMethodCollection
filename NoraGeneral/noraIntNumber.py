from importlib import reload
from PySide6 import QtCore, QtWidgets
from NoraGeneral.UI import noraIntNumberWidget
from NoraGeneral.noraUtilities import *

reload(noraIntNumberWidget)

class NoraIntNumber(QtWidgets.QDialog, noraIntNumberWidget.Ui_intNumberLayoutDialog):
    def __init__(self, parent=None):
        super(NoraIntNumber, self).__init__(parent)
        self.setParent(parent)
        self.setupUi(self)
        self.setLayout(self.intNumberLayout)
        self.start_frame = 0
        self.end_frame = 30

        self.number = 0
        self.intNumber.valueChanged.connect(self.value_changed)

    def value_changed(self):
        self.number = int(self.intNumber.value())
