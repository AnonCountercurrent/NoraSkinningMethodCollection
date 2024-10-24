from importlib import reload
from PySide6 import QtCore, QtWidgets
from NoraGeneral.UI import noraModelSelectWidget
from NoraGeneral.noraUtilities import *
from NoraGeneral import noraMDagObjectSelect

reload(noraModelSelectWidget)
reload(noraMDagObjectSelect)


class NoraModelSelect(QtWidgets.QDialog, noraModelSelectWidget.Ui_noraModelSelectedWidget):
    def __init__(self, parent=None):
        super(NoraModelSelect, self).__init__(parent)
        self.setParent(parent)
        self.setupUi(self)
        self.setLayout(self.modelSelectWithFrameRangeLayout)

        # ui
        self.apply_widget = noraMDagObjectSelect.NoraMDagObjectSelect()
        self.label_widget = noraMDagObjectSelect.NoraMDagObjectSelect()
        self.apply_widget.set_label_text("应用模型：")
        self.label_widget.set_label_text("标记模型：")
        self.modelSelectLayout.addWidget(self.apply_widget)
        self.modelSelectLayout.addWidget(self.label_widget)

