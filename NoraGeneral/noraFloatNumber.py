from importlib import reload
from PySide6 import QtCore, QtWidgets
from NoraGeneral.UI import noraFloatNumberWidget
from NoraGeneral.noraUtilities import *

reload(noraFloatNumberWidget)

class NoraFloatNumber(QtWidgets.QDialog, noraFloatNumberWidget.Ui_noraFloatNumberWidget):
    def __init__(self, default_value = 0, min_value = -65535, max_value = 65535, decimals = 2, parent=None):
        super(NoraFloatNumber, self).__init__(parent)
        self.setParent(parent)
        self.setupUi(self)
        self.setLayout(self.floatNumberLayout)

        self.doubleSpinBox.setRange(min_value, max_value)
        self.doubleSpinBox.setDecimals(decimals)
        self.number = default_value
        self.doubleSpinBox.setValue(default_value)
        self.doubleSpinBox.valueChanged.connect(self.value_changed)

    def value_changed(self):
        self.number = int(self.doubleSpinBox.value())

    def set_label_text(self, in_str):
        self.label.setText(in_str)