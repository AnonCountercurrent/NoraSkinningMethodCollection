from importlib import reload
from PySide6 import QtCore, QtWidgets
from NoraSimpleTools.UI import noraPolynomialFittingWidget
from NoraGeneral import noraMDagObjectSelect
from NoraGeneral import noraFrameRange
from NoraGeneral import noraIntNumber
from NoraGeneral import noraLoadDriverConfig
from NoraGeneral import noraChannelList

reload(noraPolynomialFittingWidget)
reload(noraMDagObjectSelect)
reload(noraFrameRange)
reload(noraLoadDriverConfig)
reload(noraChannelList)


def get_title():
    return 'Polynomial Fitting'


def get_ui():
    return NoraPolynomialFitting()


def get_width():
    return 460


def get_height():
    return 450


def get_use_custom_front_style():
    return False


class NoraPolynomialFitting(QtWidgets.QDialog, noraPolynomialFittingWidget.Ui_noraPolynomialFittingWidget):
    def __init__(self, parent=None):
        super(NoraPolynomialFitting, self).__init__(parent)
        self.setParent(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window)

        # 添加ui
        self.joint_select_widget = noraMDagObjectSelect.NoraMDagObjectSelect()
        self.joint_select_widget.set_label_text("根骨骼：")
        self.mdagSelectLayout.addWidget(self.joint_select_widget)

        self.frame_range_widget = noraFrameRange.NoraFrameRange()
        self.frameSetLayout.addWidget(self.frame_range_widget)

        self.rest_frame_widget = noraIntNumber.NoraIntNumber()
        self.rest_frame_widget.label.setText("绑定姿势所在帧：")
        self.frameSetLayout.addWidget(self.rest_frame_widget)

        self.driver_info_widget = noraLoadDriverConfig.NoraLoadDriverConfig()
        self.driverLayout.addWidget(self.driver_info_widget)

        self.driven_list_widget = noraChannelList.NoraChannelList()
        self.driven_list_widget.label.setText("Driven List: ")
        self.driverLayout.addWidget(self.driven_list_widget)
