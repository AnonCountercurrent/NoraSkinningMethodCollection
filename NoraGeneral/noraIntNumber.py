from importlib import reload
from PySide6 import QtCore, QtWidgets
from NoraGeneral.UI import noraIntNumberWidget
from NoraGeneral.noraUtilities import *

reload(noraIntNumberWidget)

class NoraIntNumber(QtWidgets.QDialog, noraIntNumberWidget.Ui_intNumberLayoutDialog):
    def __init__(self, defualt_value = 0, min_value = -65535, max_value = 65535, parent=None):
        super(NoraIntNumber, self).__init__(parent)
        self.setParent(parent)
        self.setupUi(self)
        self.setLayout(self.intNumberLayout)

        self.number = defualt_value
        self.intNumber.setValue(defualt_value)
        self.intNumber.setRange(min_value, max_value)
        self.intNumber.valueChanged.connect(self.value_changed)

    def value_changed(self):
        self.number = int(self.intNumber.value())
