from importlib import reload
from PySide2 import QtCore, QtWidgets
from NoraGeneral.UI import noraMDagNodeSelectWidget
from NoraGeneral.noraUtilities import *

reload(noraMDagNodeSelectWidget)


class NoraMDagObjectSelect(QtWidgets.QDialog, noraMDagNodeSelectWidget.Ui_noraMDagNodeSelectWidget):
    def __init__(self, parent=None):
        super(NoraMDagObjectSelect, self).__init__(parent)
        self.setParent(parent)
        self.setupUi(self)
        self.setLayout(self.selectLayout)

        # 设置图标
        arrow_back = getattr(QtWidgets.QStyle, "SP_ArrowLeft")
        self.button_icon = self.style().standardIcon(arrow_back)
        self.pushButton.setIcon(self.button_icon)

        self.dag_name = None
        self.pushButton.clicked.connect(self.get_selected_dag_object)

    def get_selected_dag_object(self):
        self.dag_name = get_selected_dag_name()
        self.lineEdit.setText(self.dag_name)

    def set_label_text(self, in_str):
        self.label.setText(in_str)


