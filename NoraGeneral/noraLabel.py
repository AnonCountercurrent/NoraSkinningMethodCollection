from importlib import reload
from PySide6 import QtCore, QtWidgets
from NoraGeneral.UI import noraLabelWidget
from NoraGeneral.noraUtilities import *

reload(noraLabelWidget)

class NoraLabel(QtWidgets.QWidget, noraLabelWidget.Ui_noraLabelLayout):
    def __init__(self, parent=None):
        super(NoraLabel, self).__init__(parent)
        self.setParent(parent)
        self.setupUi(self)
        self.setLayout(self.labelLayout)

        self.info = None
        self.info2 = None

    def set_label_text(self, text):
        self.label.setText(text)

    def get_label_text(self):
        return self.label.text()
