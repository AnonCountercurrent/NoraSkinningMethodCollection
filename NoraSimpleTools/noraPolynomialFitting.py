from importlib import reload
from PySide6 import QtCore, QtWidgets
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd

from NoraGeneral.noraUtilities import *
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
    return 580


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

        self.degree_widget = noraIntNumber.NoraIntNumber()
        self.degree_widget.label.setText("多项式的度: ")
        self.degree_widget.intNumber.setMinimum(1)
        self.degree_widget.intNumber.setMaximum(6)
        self.degree_widget.intNumber.setValue(2)
        self.degree_widget.value_changed()
        self.driverLayout.addWidget(self.degree_widget)

        self.driver_info_widget = noraLoadDriverConfig.NoraLoadDriverConfig()
        self.driverLayout.addWidget(self.driver_info_widget)

        self.driven_list_widget = noraChannelList.NoraChannelList()
        self.driven_list_widget.label.setText("被驱动列表: ")
        self.driverLayout.addWidget(self.driven_list_widget)

        # 事件绑定
        self.generateButton.clicked.connect(self.generate)

    def generate(self):
        start_frame = self.frame_range_widget.start_frame
        end_frame = self.frame_range_widget.end_frame
        if start_frame >= end_frame:
            print("error: start_frame >= end_frame")
            return
        channel_num = self.driven_list_widget.listWidget.count()
        if channel_num == 0:
            print("error: driven list is empty")
            return

        process_bar = NoraProgressBar()
        process_bar.start_progress_bar(max_value=3+channel_num)

        channels = []
        for i in range(channel_num):
            item = self.driven_list_widget.listWidget.item(i)
            item_widget = self.driven_list_widget.listWidget.itemWidget(item)
            channels.append(item_widget.info)
        if process_bar.is_progress_bar_cancelled():
            process_bar.stop_progress_bar()
            return
        process_bar.set_progress_bar_value(1)

        radians = self.radiansCheckBox.isChecked()
        driver_matrix = self.driver_info_widget.get_matrix(start_frame, end_frame, radians)
        if driver_matrix is None:
            process_bar.stop_progress_bar()
            return
        process_bar.set_progress_bar_value(2)

        driven_matrix = get_channel_matrix(channels, start_frame, end_frame, radians)
        if process_bar.is_progress_bar_cancelled():
            return
        process_bar.set_progress_bar_value(3)

        if False:
            df = pd.DataFrame(driven_matrix)
            df.to_csv(get_document_path() + r"\driven_matrix.csv")
            df = pd.DataFrame(driver_matrix)
            df.to_csv(get_document_path() + r"\driver_matrix.csv")

        lin_reg = LinearRegression()
        degree = self.degree_widget.number
        if degree == 1:
            for i in range(channel_num):
                process_bar.set_progress_bar_value(3 + i)
                y = driven_matrix[:, i]
                lin_reg.fit(driver_matrix, y)
                print(channels[i] + "--------------")
                print(lin_reg.intercept_, lin_reg.coef_)
                y_new = lin_reg.predict(driver_matrix)
                print('MSE:', mean_squared_error(y, y_new))
        else:
            poly_features = PolynomialFeatures(degree=degree, include_bias=False)
            poly_x = poly_features.fit_transform(driver_matrix)
            for i in range(channel_num):
                process_bar.set_progress_bar_value(3 + i)
                y = driven_matrix[:, i]
                lin_reg.fit(poly_x, y)
                print(channels[i] + "--------------")
                print(lin_reg.intercept_, lin_reg.coef_)
                y_new = lin_reg.predict(poly_x)
                print('MSE:', mean_squared_error(y, y_new))

        process_bar.stop_progress_bar()
