from importlib import reload
from PySide6 import QtCore, QtWidgets
from NoraGeneral.UI import noraFrameRangeWidget
from NoraGeneral.noraUtilities import *

reload(noraFrameRangeWidget)

class NoraFrameRange(QtWidgets.QDialog, noraFrameRangeWidget.Ui_noraFrameRangeDialog):
    def __init__(self, parent=None):
        super(NoraFrameRange, self).__init__(parent)
        self.setParent(parent)
        self.setupUi(self)
        self.setLayout(self.frameRangeLayout)
        self.start_frame = 0
        self.end_frame = 30

        self.leftRange.valueChanged.connect(self.start_frame_changed)
        self.rightRange.valueChanged.connect(self.end_frame_changed)

    def start_frame_changed(self):
        self.start_frame = int(self.leftRange.value())

    def end_frame_changed(self):
        self.end_frame = int(self.rightRange.value())
