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
        self.degree_widget.label.setText("多项式的度：")
        self.degree_widget.intNumber.setMinimum(1)
        self.degree_widget.intNumber.setMaximum(16)
        self.degree_widget.intNumber.setValue(2)
        self.degree_widget.value_changed()
        self.driverLayout.addWidget(self.degree_widget)

        self.driver_info_widget = noraLoadDriverConfig.NoraLoadDriverConfig()
        self.driverLayout.addWidget(self.driver_info_widget)

        self.driven_list_widget = noraChannelList.NoraChannelList()
        self.driven_list_widget.label.setText("被驱动列表：")
        self.driverLayout.addWidget(self.driven_list_widget)

        # 事件绑定
        self.generateButton.clicked.connect(self.generate)
        self.printPushButton.clicked.connect(self.print_coefficients)

    def generate(self):
        # 帧数范围
        start_frame = self.frame_range_widget.start_frame
        end_frame = self.frame_range_widget.end_frame
        rest_frame = self.rest_frame_widget.number
        if start_frame >= end_frame:
            print("error: start_frame >= end_frame")
            return
        if rest_frame < start_frame or rest_frame >= end_frame:
            print("error: rest_frame < start_frame or rest_frame >= end_frame")
            return
        channel_num = self.driven_list_widget.listWidget.count()
        if channel_num == 0:
            print("error: driven list is empty")
            return
        process_bar = NoraProgressBar()
        process_bar.start_progress_bar(max_value=4 + channel_num)
        # 被驱动channel列表
        channels = []
        for i in range(channel_num):
            item = self.driven_list_widget.listWidget.item(i)
            item_widget = self.driven_list_widget.listWidget.itemWidget(item)
            channels.append(item_widget.info)
        if process_bar.is_progress_bar_cancelled():
            process_bar.stop_progress_bar()
            return
        process_bar.set_progress_bar_value(1)
        # 驱动数据
        radians = self.radiansCheckBox.isChecked()
        driver_matrix = self.driver_info_widget.get_matrix(start_frame, end_frame, radians)
        if driver_matrix is None:
            process_bar.stop_progress_bar()
            return
        driver_channels = self.driver_info_widget.get_channel_names()
        process_bar.set_progress_bar_value(2)
        # 被驱动标记
        driven_matrix = get_channel_matrix(channels, start_frame, end_frame, radians)
        if process_bar.is_progress_bar_cancelled():
            return
        process_bar.set_progress_bar_value(3)
        # 输出标记到CSV观测
        if self.csvCheckBox.isChecked():
            df = pd.DataFrame(driven_matrix)
            df.to_csv(get_document_path() + r"\driven_matrix.csv")
            df = pd.DataFrame(driver_matrix)
            df.to_csv(get_document_path() + r"\driver_matrix.csv")
        process_bar.set_progress_bar_value(4)
        # 线性回归
        lin_reg = LinearRegression()
        degree = self.degree_widget.number
        poly_features = PolynomialFeatures(degree=degree, include_bias=False)
        poly_x = poly_features.fit_transform(driver_matrix)
        for i in range(channel_num):
            process_bar.set_progress_bar_value(4 + i)
            y = driven_matrix[:, i]
            lin_reg.fit(poly_x, y)
            y_new = lin_reg.predict(poly_x)
            print(channels[i] + "--------------")
            print('MSE:', mean_squared_error(y, y_new))
            print('intercept:', lin_reg.intercept_)
            print('coefficients:', lin_reg.coef_)
            if self.genDriverNodeCheckBox.isChecked():
                self.custom_create_node(driver_channels, channels[i], degree, driven_matrix[rest_frame, i], lin_reg.intercept_, lin_reg.coef_, radians)

        process_bar.stop_progress_bar()

    @staticmethod
    def custom_create_node(input_channels:list, output_channel:str, degree:int, default_value:float, intercept:float, coefficients:np.ndarray, radians=False):
        """
        用于创建这个节点
        """
        driver_num = len(input_channels)
        # 创建节点和连线
        node_name = cmds.createNode("noraPolynomialFitting")
        for i in range(driver_num):
            cmds.connectAttr(input_channels[i], f"{node_name}.inputValues[{i}]")
            if radians and is_rotation_attribute(input_channels[i]):
                cmds.setAttr(f"{node_name}.radians[{i}]", True)
            else:
                cmds.setAttr(f"{node_name}.radians[{i}]", False)
        cmds.connectAttr(f"{node_name}.outputValue", output_channel, force=True)
        # 数据写入
        cmds.setAttr(f"{node_name}.defaultValue", default_value)
        cmds.setAttr(f"{node_name}.degree", degree)
        cmds.setAttr(f"{node_name}.intercept", intercept)
        for i in range(coefficients.size):
            cmds.setAttr(f"{node_name}.coefficients[{i}]", coefficients[i])
        cmds.setAttr(f"{node_name}.activated", True)

    @staticmethod
    def custom_create_node_om(input_channels:list, output_channel:str, degree:int, default_value:float, intercept:float, coefficients:np.ndarray, radians=False):
        dg_modifier = om.MDGModifier()
        driver_num = len(input_channels)
        # 创建节点
        node_obj = dg_modifier.createNode("noraPolynomialFitting")
        dg_node = om.MFnDependencyNode(node_obj)
        # 数据写入
        dg_node.findPlug("defaultValue", False).setDouble(default_value)
        dg_node.findPlug("degree", False).setInt(degree)
        dg_node.findPlug("intercept", False).setDouble(intercept)
        coeff_plug = dg_node.findPlug("coefficients", False)
        for i in range(coefficients.size):
            coeff_plug.elementByLogicalIndex(i).setDouble(coefficients[i])
        radians_plug = dg_node.findPlug("radians", False)
        for i in range(driver_num):
            if radians and is_rotation_attribute(input_channels[i]):
                radians_plug.elementByLogicalIndex(i).setBool(True)
            else:
                radians_plug.elementByLogicalIndex(i).setBool(False)
        # 连线
        in_plug = dg_node.findPlug("inputValues", False)
        for i in range(driver_num):
            driver_node_attr = input_channels[i].split('.')
            driver_node = get_dg_node_by_name(driver_node_attr[0])
            driver_plug = driver_node.findPlug(driver_node_attr[1], False)
            in_plug_item = in_plug.elementByLogicalIndex(i)
            dg_modifier.connect(driver_plug, in_plug_item)
        output_node_attr = output_channel.split('.')
        out_plug = dg_node.findPlug("outputValue", False)
        output_node = get_dg_node_by_name(output_node_attr[0])
        output_plug = output_node.findPlug(output_node_attr[1], False)
        # 检查输出目标是否已经被连了
        if output_plug.isDestination:
            current_connection = output_plug.source()
            dg_modifier.disconnect(current_connection, output_plug)
        dg_modifier.connect(out_plug, output_plug)
        # 执行
        dg_node.findPlug("activated", False).setBool(True)
        dg_modifier.doIt()

    @staticmethod
    def print_coefficients(self):
        final_string = "("
        handled_channels = 0
        selected_objects = cmds.ls(selection=True, long=True, objectsOnly=True)
        for obj in selected_objects:
            channels = cmds.listAttr(obj, keyable=True, scalar=True, visible=True, settable=True, inUse=True)
            if channels:
                for long_channel_name in channels:
                    full_path_name = obj + '.' + long_channel_name
                    # 跳过上锁的
                    locked = cmds.getAttr(full_path_name, lock=True)
                    if locked:
                        continue
                    # Channel是否连接到了 dg node noraPolynomialFitting
                    connected_nodes = cmds.listConnections(full_path_name, source=True, destination=False, plugs=True)
                    if connected_nodes:
                        for node in connected_nodes:
                            # 检查节点类型是否是 noraPolynomialFitting
                            node_name, attr = node.split('.', 1)
                            if cmds.nodeType(node_name) == 'noraPolynomialFitting':
                                print(replace_fbx_asc_xxx(get_short_name(obj), True) + '.' + long_channel_name)
                                print("intercept: " + get_split_float_str(cmds.getAttr(node_name + ".intercept")))
                                coef_indices = cmds.getAttr(node_name + ".coefficients", multiIndices=True)
                                if coef_indices is None:
                                    print("coefficients: None")
                                    continue
                                if handled_channels > 0:
                                    final_string += ","
                                final_string += "(Intercept=" + get_split_float_str(cmds.getAttr(node_name + ".intercept")) + ",Coefficients="
                                coef_num = len(coef_indices)
                                coefficients_str = "("
                                for i in range(coef_num):
                                    coefficients_str += get_split_float_str(cmds.getAttr(node_name + f".coefficients[{i}]"))
                                    if i < coef_num - 1:
                                        coefficients_str += ","
                                coefficients_str += "))"
                                final_string += coefficients_str
                                print("coefficients: " + coefficients_str)
                                handled_channels += 1
        final_string += ")"
        print(final_string)
