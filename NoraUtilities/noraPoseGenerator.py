from importlib import reload
from PySide6 import QtCore, QtGui, QtWidgets
from NoraUtilities.UI import noraPoseGeneratorWidget
from NoraUtilities.UI import noraPoseGeneratorWindow
from NoraUtilities.UI import noraChannelSelectWindow
from NoraUtilities.UI import noraPoseGenSettingsWindow
from NoraGeneral import noraUtilities
from NoraGeneral.noraUtilities import *
from NoraGeneral.noraQtHelpers import QtHelpers
import maya.cmds as cmds
import json
from dataclasses import dataclass
import random
import maya.api.OpenMaya as om
import maya.api.OpenMayaAnim as oma
import numpy as np
import itertools

reload(noraUtilities)
reload(noraPoseGeneratorWidget)
reload(noraPoseGeneratorWindow)
reload(noraChannelSelectWindow)
reload(noraPoseGenSettingsWindow)


def get_title():
    return 'Pose Generator'


def get_ui():
    return NoraPoseGenerator()


def get_width():
    return 460


def get_height():
    return 300


def get_use_custom_front_style():
    return False


class NoraPoseGenerator(QtWidgets.QDialog, noraPoseGeneratorWidget.Ui_noraPoseGeneratorWidget):
    def __init__(self):
        super(NoraPoseGenerator, self).__init__()
        self.setParent(get_maya_main_window())
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window)

        # 成员
        self.pose_gen_win = None

        # 事件
        self.openPoseGenerator.clicked.connect(self.open_pose_generator)

    def open_pose_generator(self):
        if cmds.window('noraPoseGenWin', ex=True):
            cmds.deleteUI('noraPoseGenWin')
        self.pose_gen_win = NoraPoseGeneratorWin()
        self.pose_gen_win.show()


@dataclass
class NoraChannelMinMaxValue:
    name: str
    min_value: float
    max_value: float
    sample_num: int


@dataclass
class NoraPoseGeneratorConfig:
    channels: list
    channel_min_max_values: list
    num_samples: int
    start_frame: int
    controller_probability: int
    distribution: str
    sigma: float

    def set_default_min_max_values(self):
        self.channel_min_max_values.append(NoraChannelMinMaxValue('rotateX', -90.0, 90.0, 1))
        self.channel_min_max_values.append(NoraChannelMinMaxValue('rotateY', -90.0, 90.0, 1))
        self.channel_min_max_values.append(NoraChannelMinMaxValue('rotateZ', -90.0, 90.0, 1))

    def find_channel_min_max(self, attribute_name):
        """
        参数最大值最小值
        """
        results = [channel for channel in self.channel_min_max_values if
                   channel.name.lower() == attribute_name.lower()]
        if len(results) > 0:
            return results[-1]
        return None


@dataclass
class ChannelInfo:
    name: str
    display_name: str
    default_value: float
    min_value: float
    max_value: float
    object_type: str
    group_name: str
    channel_name: str
    sample_num: int


class NoraPoseGenConfigJsonEncoder(json.JSONEncoder):
    """
    用于存json
    """
    def default(self, obj):
        if isinstance(obj, NoraPoseGeneratorConfig) or isinstance(obj, ChannelInfo) or isinstance(obj, NoraChannelMinMaxValue):
            return obj.__dict__
        else:
            return json.JSONEncoder.default(self, object)


class NoraPoseGenSettingsWindow(QtWidgets.QMainWindow, noraPoseGenSettingsWindow.Ui_noraPoseGenSettingsWindow):
    def __init__(self, parent, config: NoraPoseGeneratorConfig):
        super(NoraPoseGenSettingsWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Settings')
        self.setObjectName("noraPoseGenSettingsWin")
        self.setWindowIcon(QtGui.QIcon(get_icon_path("Nora_Valkyrie_Emblem_128.png")))
        self.setCentralWidget(self.mainWidget)

        self.config = config

        self.init_table()
        self.refresh_table()

        self.addButton.clicked.connect(self.add_button_click)
        self.saveButton.clicked.connect(self.save_button_click)

    def init_table(self):
        """
        初始化表格
        """
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['Name', 'Min', 'Max', 'Num'])
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        for col in range(self.tableWidget.columnCount()):
            self.tableWidget.horizontalHeader().setSectionResizeMode(col, QtWidgets.QHeaderView.ResizeToContents)
        table_width = self.tableWidget.geometry().width()
        self.tableWidget.setColumnWidth(0, table_width * 0.5)
        self.tableWidget.setColumnWidth(1, table_width * 0.1)
        self.tableWidget.setColumnWidth(2, table_width * 0.1)
        self.tableWidget.setColumnWidth(3, table_width * 0.1)
        self.tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignLeft)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        self.tableWidget.setShowGrid(True)
        # 一选选一行
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        # 右击菜单事件绑定
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.on_table_context_menu)

    def refresh_table(self):
        """
        刷新表
        """
        self.tableWidget.setRowCount(len(self.config.channel_min_max_values))
        for row, parameter in enumerate(self.config.channel_min_max_values):
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(parameter.name))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(parameter.min_value)))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(parameter.max_value)))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(parameter.sample_num)))
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)

    def on_table_context_menu(self, point):
        """
        右击时的菜单
        """
        if self.tableWidget.rowCount() == 0:
            return
        # 添加移除和清理
        menu = QtWidgets.QMenu(self)
        selected_indices = self.get_selected_attribute_indices()
        clear_action = menu.addAction('清空')
        if selected_indices:
            menu.addSeparator()
        remove_selected_action = None
        if len(selected_indices) > 0:
            remove_selected_action = menu.addAction('删除选择的行')
        # 获取菜单的操作
        action = menu.exec_(self.mapToGlobal(point))
        if action:
            if remove_selected_action and action == remove_selected_action:
                self.remove_selected_attributes()
            elif action == clear_action:
                self.remove_all()
        self.tableWidget.clearSelection()

    def remove_selected_attributes(self):
        """
        移除选中的行
        """
        remove_list = self.get_selected_attribute_indices()
        self.remove_line_by_indices(remove_list)

    def remove_all(self):
        self.remove_line_by_indices([i for i in range(self.tableWidget.rowCount())])

    def remove_line_by_indices(self, remove_list):
        """
        从下往上移除行
        """
        for index in sorted(remove_list, reverse=True):
            self.tableWidget.removeRow(index)

    def get_selected_attribute_indices(self):
        """
        获取选中的行号
        """
        resulting_indices = list()
        selected_items = self.tableWidget.selectedItems()
        col_count = self.tableWidget.columnCount()
        num_selected_rows = int(len(selected_items) / col_count)
        for i in range(0, num_selected_rows):
            item = selected_items[i * col_count]
            resulting_indices.append(item.row())
        return resulting_indices

    def add_button_click(self):
        """
        添加一行
        """
        row_count = self.tableWidget.rowCount()
        self.tableWidget.setRowCount(row_count + 1)
        self.tableWidget.setItem(row_count, 0, QtWidgets.QTableWidgetItem("None"))
        self.tableWidget.setItem(row_count, 1, QtWidgets.QTableWidgetItem(str(0)))
        self.tableWidget.setItem(row_count, 2, QtWidgets.QTableWidgetItem(str(1)))
        self.tableWidget.setItem(row_count, 3, QtWidgets.QTableWidgetItem(str(1)))

    def save_button_click(self):
        """
        保存到config
        """
        self.config.channel_min_max_values.clear()
        row_count = self.tableWidget.rowCount()
        for row in range(row_count):
            limit = NoraChannelMinMaxValue(self.tableWidget.item(row, 0).text(),
                                           float(self.tableWidget.item(row, 1).text()),
                                           float(self.tableWidget.item(row, 2).text()),
                                           int(self.tableWidget.item(row, 3).text()))
            self.config.channel_min_max_values.append(limit)


class NoraChannelSelectWindow(QtWidgets.QMainWindow, noraChannelSelectWindow.Ui_noraChannelSelectWindow):
    """
    这里将父类设为QMainWindow，并设置父对象，这样做可以让这个通道选择窗体在
    """

    def __init__(self, parent, config: NoraPoseGeneratorConfig):
        super(NoraChannelSelectWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Add Channels')
        self.setObjectName("noraAddChannelsWin")
        self.setWindowIcon(QtGui.QIcon(get_icon_path("Nora_Valkyrie_Emblem_128.png")))
        self.setCentralWidget(self.mainWidget)
        self.pushButton.clicked.connect(self.add_channels)

        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        self.config = config
        self.generator = parent
        self.selected_objects = None
        self.current_channels = list()

        self.deal_with_selects()

    def deal_with_selects(self):
        """
        收集选中对象的属性，将属性总结到列表
        """
        self.current_channels.clear()
        self.selected_objects = cmds.ls(selection=True, long=True, objectsOnly=True)
        for obj in self.selected_objects:
            channels = cmds.listAttr(obj, keyable=True, scalar=True, visible=True, settable=True, inUse=True)
            if channels:
                for long_channel_name in channels:
                    full_path_name = obj + '.' + long_channel_name

                    # 跳过上锁的
                    locked = cmds.getAttr(full_path_name, lock=True)
                    if locked:
                        continue
                    # 跳过已经添加的
                    if any(x.name == full_path_name for x in self.config.channels):
                        continue

                    # 尝试设置一个取值范围
                    # channel 的取值范围
                    default_value, min_value, max_value = get_attribute_values(long_channel_name, obj)
                    # 配置的取值范围
                    attribute_min_max = self.config.find_channel_min_max(long_channel_name)
                    if not min_value:
                        min_value = attribute_min_max.min_value if attribute_min_max else 0.0
                    if not max_value:
                        max_value = attribute_min_max.max_value if attribute_min_max else 1.0
                    sample_num = attribute_min_max.sample_num if attribute_min_max else 1
                    object_type = cmds.objectType(obj)
                    # joint的约束信息最优先
                    has_limit_info, limit_info = get_rotation_limits(obj, object_type)
                    if has_limit_info:
                        min_value, max_value = apply_maya_limits(long_channel_name, limit_info, min_value, max_value)

                    # 添加到当前Channel列表
                    channel_info = ChannelInfo(full_path_name,
                                               get_short_name(obj) + '.' + long_channel_name,
                                               default_value,
                                               min_value,
                                               max_value,
                                               object_type,
                                               get_attribute_group_name(long_channel_name, obj),
                                               long_channel_name,
                                               sample_num)
                    self.current_channels.append(channel_info)

        # 将Channel名去掉重复的显示出来
        channel_names = list()
        for c in self.current_channels:
            if c.channel_name not in channel_names:
                channel_names.append(c.channel_name)
                self.listWidget.addItem(c.channel_name)

    def add_channels(self):
        """
        将选中的属性增加到生成器窗体
        """
        # 筛选出要添加的channel
        selected_items = self.listWidget.selectedItems()
        if len(selected_items) == 0:
            pass
        selected_channel_names = list()
        for item in selected_items:
            selected_channel_names.append(item.text())
        channels_to_add = list()
        for channel_info in self.current_channels:
            if any(channel_info.channel_name == x for x in selected_channel_names):
                channels_to_add.append(channel_info)
        # 添加到列表
        self.config.channels.extend(channels_to_add)
        if len(self.config.channels) > 0:
            self.config.channels.sort(key=lambda x: x.display_name.lower())
        # 刷新ui
        self.generator.refresh_table()
        # 关闭自己
        self.close()


class NoraPoseGeneratorWin(QtWidgets.QDialog, noraPoseGeneratorWindow.Ui_noraPoseGeneratorWindow):
    table_column__name = 0
    table_column__default = 1
    table_column__minimum = 2
    table_column__maximum = 3
    table_column__object_type = 4
    table_column__group_name = 5
    table_column__samples = 6

    min_label_text_width = 160
    main_button_size = 22

    def __init__(self):
        super(NoraPoseGeneratorWin, self).__init__()
        self.setParent(get_maya_main_window())
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowTitle('Nora Pose Generator')
        self.setObjectName("noraPoseGenWin")
        self.setWindowIcon(QtGui.QIcon(get_icon_path("Nora_Valkyrie_Emblem_128.png")))

        # Channels 表格设置
        self.init_table_widget()

        # 添加一些参数显示/输入
        _, self.selected_parameter_name_widget = QtHelpers.add_string_field(layout=self.ChannelPropertiesLayout,
                                                                            row_index=0,
                                                                            name='通道名:', value='',
                                                                            min_label_text_width=self.min_label_text_width)
        _, self.selected_parameter_default_widget = QtHelpers.add_float_field(layout=self.ChannelPropertiesLayout,
                                                                              row_index=1,
                                                                              name='默认值:', value=0.0, decimals=3,
                                                                              min_label_text_width=self.min_label_text_width)
        _, self.selected_parameter_minimum_widget = QtHelpers.add_float_field(layout=self.ChannelPropertiesLayout,
                                                                              row_index=2,
                                                                              name='最小值:', value=0.0, decimals=3,
                                                                              min_label_text_width=self.min_label_text_width)
        _, self.selected_parameter_maximum_widget = QtHelpers.add_float_field(layout=self.ChannelPropertiesLayout,
                                                                              row_index=3,
                                                                              name='最大值:', value=1.0, decimals=3,
                                                                              min_label_text_width=self.min_label_text_width)
        _, self.selected_group_name_widget = QtHelpers.add_string_field(layout=self.ChannelPropertiesLayout,
                                                                        row_index=4,
                                                                        name='组名:', value='',
                                                                        min_label_text_width=self.min_label_text_width)
        _, self.selected_parameter_samples_widget = QtHelpers.add_int_field(layout=self.ChannelPropertiesLayout,
                                                                            row_index=5,
                                                                            name='采样数:', value=6, min_value=1, max_value=100,
                                                                            min_label_text_width=self.min_label_text_width)
        self.selected_parameter_name_widget.setReadOnly(True)
        self.selected_parameter_default_widget.setReadOnly(True)

        # 工具栏设置
        dialog_save_button = getattr(QtWidgets.QStyle, "SP_DialogSaveButton")
        file_dialog_end = getattr(QtWidgets.QStyle, "SP_DialogOpenButton")
        browser_reload = getattr(QtWidgets.QStyle, "SP_BrowserReload")
        save_icon = self.style().standardIcon(dialog_save_button)
        open_icon = self.style().standardIcon(file_dialog_end)
        refresh_icon = self.style().standardIcon(browser_reload)
        self.saveButton.setIcon(save_icon)
        self.readButton.setIcon(open_icon)
        self.refreshButton.setIcon(refresh_icon)
        self.addButton.setIcon(QtGui.QIcon(get_icon_path("add.png")))
        self.settingsButton.setIcon(QtGui.QIcon(get_icon_path("settings.png")))
        self.LastConfigPath.setReadOnly(True)

        # 工具栏事件绑定
        self.saveButton.clicked.connect(self.save_config)
        self.readButton.clicked.connect(self.open_config)
        self.refreshButton.clicked.connect(self.refresh_config)
        self.settingsButton.clicked.connect(self.open_settings_win)
        self.addButton.clicked.connect(self.add_channels)
        # 参数修改相关事件绑定
        self.tableWidget.itemSelectionChanged.connect(self.on_parameter_selection_changed)
        self.selected_parameter_minimum_widget.valueChanged.connect(self.on_selected_parameter_min_value_changed)
        self.selected_parameter_maximum_widget.valueChanged.connect(self.on_selected_parameter_max_value_changed)
        self.selected_group_name_widget.textChanged.connect(self.on_selected_group_name_changed)
        self.selected_parameter_samples_widget.valueChanged.connect(self.on_selected_parameter_samples_value_changed)

        # 成员
        self.add_channels_win = None
        self.settings_win = None
        self.json_data = None
        self.process_bar = NoraProgressBar()
        self.config = NoraPoseGeneratorConfig(list(), list(), 15000, 0, 85, "normal", 1.5)
        self.config.set_default_min_max_values()

        # 添加一些生成设置
        _, self.generator_settings_num_samples_widget = QtHelpers.add_int_field(layout=self.GeneratorSettingsLayout,
                                                                                row_index=0,
                                                                                name='帧数:',
                                                                                value=self.config.num_samples,
                                                                                min_value=1,
                                                                                min_label_text_width=self.min_label_text_width)
        _, self.generator_settings_start_frame_widget = QtHelpers.add_int_field(layout=self.GeneratorSettingsLayout,
                                                                                row_index=1,
                                                                                name='起始帧:',
                                                                                value=self.config.start_frame,
                                                                                min_label_text_width=self.min_label_text_width)
        _, self.generator_settings_distribution_widget = QtHelpers.add_combo_box_field(layout=self.GeneratorSettingsLayout,
                                                                                       row_index=2,
                                                                                       name='分布函数:',
                                                                                       combo_items=["normal", "uniform", "combination"],
                                                                                       min_label_text_width=self.min_label_text_width)
        self.generator_settings_controller_probability_label_widget, self.generator_settings_controller_probability_widget = QtHelpers.add_int_field(layout=self.GeneratorSettingsLayout,
                                                                                                                                                     row_index=3,
                                                                                                                                                     name='随机比例:',
                                                                                                                                                     value=self.config.controller_probability,
                                                                                                                                                     min_value=0, max_value=100,
                                                                                                                                                     min_label_text_width=self.min_label_text_width)
        self.generator_settings_controller_probability_widget.setSuffix(' %')
        self.generator_settings_normal_sigma_label_widget, self.generator_settings_normal_sigma_widget = QtHelpers.add_float_field(layout=self.GeneratorSettingsLayout,
                                                                                                                                   row_index=4,
                                                                                                                                   name='标准差:',
                                                                                                                                   value=self.config.sigma,
                                                                                                                                   min_label_text_width=self.min_label_text_width)
        # 生成参数相关事件
        self.generator_settings_num_samples_widget.valueChanged.connect(self.on_generator_settings_num_samples_changed)
        self.generator_settings_start_frame_widget.valueChanged.connect(self.on_generator_settings_start_frame_changed)
        self.generator_settings_controller_probability_widget.valueChanged.connect(self.on_generator_settings_controller_probability_changed)
        self.generator_settings_distribution_widget.currentTextChanged.connect(self.on_generator_settings_distribution_changed)
        self.generator_settings_normal_sigma_widget.valueChanged.connect(self.on_generator_settings_normal_sigma_changed)
        self.GenerateButton.clicked.connect(self.generate_poses)

        # 使右侧不会随缩放窗体拉伸
        self.splitter.setStretchFactor(0, 1)
        self.splitter.setStretchFactor(1, 0)

    def init_table_widget(self):
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['Parameter Name', 'Default', 'Min', 'Max', 'Object Type', 'Group', 'Sample Num'])
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        for col in range(self.tableWidget.columnCount()):
            self.tableWidget.horizontalHeader().setSectionResizeMode(col, QtWidgets.QHeaderView.ResizeToContents)
        table_width = self.tableWidget.geometry().width()
        self.tableWidget.setColumnWidth(self.table_column__name, table_width * 0.5)
        self.tableWidget.setColumnWidth(self.table_column__default, table_width * 0.1)
        self.tableWidget.setColumnWidth(self.table_column__minimum, table_width * 0.1)
        self.tableWidget.setColumnWidth(self.table_column__maximum, table_width * 0.1)
        self.tableWidget.setColumnWidth(self.table_column__object_type, table_width * 0.2)
        self.tableWidget.setColumnWidth(self.table_column__group_name, table_width * 0.2)
        self.tableWidget.setColumnWidth(self.table_column__samples, table_width * 0.1)
        self.tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignLeft)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        self.tableWidget.setShowGrid(True)
        # self.tableWidget.setColumnWidth(self.table_column__name, 450)
        # 一选选一行，不直接编辑
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # 右击菜单事件绑定
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.on_table_context_menu)

    @staticmethod
    def get_default_config_path():
        # 默认保存路径
        path = get_document_path() + r'\Nora Skinning Method Collection'
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def save_config(self):
        save_path = self.get_default_config_path()
        # 对话框
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            parent=self,
            caption='保存配置',
            dir=save_path + r'\pose_generator_config',
            filter='Configuration Files (*.json)')
        # 保存
        if len(file_path) > 0:
            json_string = json.dumps(self.config, sort_keys=True, indent=4, cls=NoraPoseGenConfigJsonEncoder)
            self.LastConfigPath.setText(file_path)
            self.json_data = json.loads(json_string)
            with open(file_path, 'wt') as writeFile:
                writeFile.writelines(json_string)

    def open_config(self):
        open_path = self.get_default_config_path()
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            parent=self,
            caption='读取配置',
            dir=open_path,
            filter='Configuration Files (*.json)')

        if len(file_path) > 0:
            try:
                with open(file_path, 'rt') as readFile:
                    self.json_data = json.load(readFile)
                    self.LastConfigPath.setText(file_path)
                    self.refresh_config()
            except ValueError as e:
                self.json_data = None
                self.LastConfigPath.setText("")
                print(e)

    def refresh_config(self):
        if not self.json_data:
            pass
        self.config = NoraPoseGeneratorConfig([],
                                              [],
                                              self.json_data['num_samples'],
                                              self.json_data['start_frame'],
                                              self.json_data['controller_probability'],
                                              self.json_data['distribution'],
                                              self.json_data['sigma'])
        channels_list = self.json_data['channels']
        for c in channels_list:
            self.config.channels.append(ChannelInfo(**c))
        channel_limit = self.json_data['channel_min_max_values']
        for c in channel_limit:
            self.config.channel_min_max_values.append(NoraChannelMinMaxValue(**c))
        self.refresh_table()
        self.generator_settings_num_samples_widget.setValue(self.config.num_samples)
        self.generator_settings_start_frame_widget.setValue(self.config.start_frame)
        self.generator_settings_controller_probability_widget.setValue(self.config.controller_probability)
        self.generator_settings_distribution_widget.setCurrentText(self.config.distribution)
        self.generator_settings_normal_sigma_widget.setValue(self.config.sigma)

    def add_channels(self):
        # 弹出Channel选择窗体
        if cmds.window('noraAddChannelsWin', ex=True):
            cmds.deleteUI('noraAddChannelsWin')
        self.add_channels_win = NoraChannelSelectWindow(self, self.config)
        self.add_channels_win.show()

    def open_settings_win(self):
        # 弹出设置窗体
        if cmds.window('noraPoseGenSettingsWin', ex=True):
            cmds.deleteUI('noraPoseGenSettingsWin')
        self.settings_win = NoraPoseGenSettingsWindow(self, self.config)
        self.settings_win.show()

    def refresh_table(self):
        """
        刷新表
        """
        self.tableWidget.setRowCount(len(self.config.channels))
        for row, parameter in enumerate(self.config.channels):
            param_name_item = QtWidgets.QTableWidgetItem(parameter.display_name)
            self.tableWidget.setItem(row, self.table_column__name, param_name_item)
            self.tableWidget.setItem(row, self.table_column__default,
                                     QtWidgets.QTableWidgetItem(str(parameter.default_value)))
            self.tableWidget.setItem(row, self.table_column__minimum,
                                     QtWidgets.QTableWidgetItem(str(parameter.min_value)))
            self.tableWidget.setItem(row, self.table_column__maximum,
                                     QtWidgets.QTableWidgetItem(str(parameter.max_value)))
            self.tableWidget.setItem(row, self.table_column__object_type,
                                     QtWidgets.QTableWidgetItem(parameter.object_type))
            self.tableWidget.setItem(row, self.table_column__group_name,
                                     QtWidgets.QTableWidgetItem(parameter.group_name))
            self.tableWidget.setItem(row, self.table_column__samples,
                                     QtWidgets.QTableWidgetItem(str(parameter.sample_num)))
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)

    def on_table_context_menu(self, point):
        """
        右击时的菜单
        """
        if self.tableWidget.rowCount() == 0:
            return
        # 添加移除和清理
        menu = QtWidgets.QMenu(self)
        selected_indices = self.get_selected_attribute_indices()
        clear_action = menu.addAction('清空')
        if selected_indices:
            menu.addSeparator()
        remove_selected_action = None
        if len(selected_indices) > 0:
            remove_selected_action = menu.addAction('删除选择的行')
        # 获取菜单的操作
        action = menu.exec_(self.mapToGlobal(point))
        if action:
            if remove_selected_action and action == remove_selected_action:
                self.remove_selected_attributes()
            elif action == clear_action:
                self.remove_all()
        self.tableWidget.clearSelection()

    def remove_all(self):
        self.remove_line_by_indices([i for i in range(self.tableWidget.rowCount())])

    def remove_selected_attributes(self):
        """
        移除选中的行
        """
        remove_list = self.get_selected_attribute_indices()
        self.remove_line_by_indices(remove_list)

    def remove_line_by_indices(self, remove_list):
        """
        从表格和config中，从下往上移除行
        """
        channels_to_remove = list()
        for index in sorted(remove_list, reverse=True):
            channels_to_remove.append(self.tableWidget.item(index, 0).text())
            self.tableWidget.removeRow(index)
        channels_num = len(self.config.channels)
        for i in [channels_num - c - 1 for c in range(channels_num)]:
            if any(x == self.config.channels[i].display_name for x in channels_to_remove):
                self.config.channels.pop(i)

    def get_selected_attribute_indices(self):
        """
        获取选中的行号
        """
        resulting_indices = list()
        selected_items = self.tableWidget.selectedItems()
        col_count = self.tableWidget.columnCount()
        num_selected_rows = int(len(selected_items) / col_count)
        for i in range(0, num_selected_rows):
            item = selected_items[i * col_count]
            resulting_indices.append(item.row())
        return resulting_indices

    def get_channel_info_by_display_name(self, display_name):
        """
        通过显示名，获取参数
        """
        for c in self.config.channels:
            if c.display_name == display_name:
                return c
        return None

    def on_parameter_selection_changed(self):
        """
        选中参数变更
        """
        # 先把事件通知关了
        self.selected_parameter_name_widget.blockSignals(True)
        self.selected_parameter_default_widget.blockSignals(True)
        self.selected_parameter_minimum_widget.blockSignals(True)
        self.selected_parameter_maximum_widget.blockSignals(True)
        self.selected_group_name_widget.blockSignals(True)

        selected_param_indices = self.get_selected_attribute_indices()
        if len(selected_param_indices) > 0:
            display_name = self.tableWidget.item(selected_param_indices[-1], 0).text()
            parameter = self.get_channel_info_by_display_name(display_name)
            self.selected_parameter_name_widget.setText(parameter.display_name)
            self.selected_parameter_default_widget.setValue(parameter.default_value)
            self.selected_parameter_minimum_widget.setValue(parameter.min_value)
            self.selected_parameter_maximum_widget.setValue(parameter.max_value)
            self.selected_group_name_widget.setText(parameter.group_name)
            self.selected_parameter_samples_widget.setValue(parameter.sample_num)
        else:
            self.selected_parameter_name_widget.setText('')
            self.selected_parameter_default_widget.setValue(0.0)
            self.selected_parameter_minimum_widget.setValue(0.0)
            self.selected_parameter_maximum_widget.setValue(1.0)
            self.selected_group_name_widget.setText('')
            self.selected_parameter_samples_widget.setValue(1)

        self.selected_parameter_name_widget.blockSignals(False)
        self.selected_parameter_default_widget.blockSignals(False)
        self.selected_parameter_minimum_widget.blockSignals(False)
        self.selected_parameter_maximum_widget.blockSignals(False)
        self.selected_group_name_widget.blockSignals(False)

    def on_selected_parameter_min_value_changed(self):
        selected_param_indices = self.get_selected_attribute_indices()
        for index in selected_param_indices:
            display_name = self.tableWidget.item(index, 0).text()
            parameter = self.get_channel_info_by_display_name(display_name)
            new_value = self.selected_parameter_minimum_widget.value()
            parameter.min_value = new_value
            self.tableWidget.item(index, self.table_column__minimum).setText(str(new_value))

    def on_selected_parameter_max_value_changed(self):
        selected_param_indices = self.get_selected_attribute_indices()
        for index in selected_param_indices:
            display_name = self.tableWidget.item(index, 0).text()
            parameter = self.get_channel_info_by_display_name(display_name)
            new_value = self.selected_parameter_maximum_widget.value()
            parameter.max_value = new_value
            self.tableWidget.item(index, self.table_column__maximum).setText(str(new_value))

    def on_selected_group_name_changed(self):
        selected_param_indices = self.get_selected_attribute_indices()
        for index in selected_param_indices:
            display_name = self.tableWidget.item(index, 0).text()
            parameter = self.get_channel_info_by_display_name(display_name)
            new_value = self.selected_group_name_widget.text()
            parameter.group_name = new_value
            self.tableWidget.item(index, self.table_column__group_name).setText(str(new_value))

    def on_selected_parameter_samples_value_changed(self):
        selected_param_indices = self.get_selected_attribute_indices()
        for index in selected_param_indices:
            display_name = self.tableWidget.item(index, 0).text()
            parameter = self.get_channel_info_by_display_name(display_name)
            new_value = self.selected_parameter_samples_widget.value()
            parameter.sample_num = new_value
            self.tableWidget.item(index, self.table_column__samples).setText(str(new_value))

    def on_generator_settings_num_samples_changed(self):
        self.config.num_samples = self.generator_settings_num_samples_widget.value()

    def on_generator_settings_start_frame_changed(self):
        self.config.start_frame = self.generator_settings_start_frame_widget.value()

    def on_generator_settings_controller_probability_changed(self):
        self.config.controller_probability = self.generator_settings_controller_probability_widget.value()

    def on_generator_settings_distribution_changed(self):
        self.config.distribution = self.generator_settings_distribution_widget.currentText()
        if self.config.distribution == "normal":
            self.generator_settings_normal_sigma_widget.setVisible(True)
            self.generator_settings_normal_sigma_label_widget.setVisible(True)
            self.generator_settings_controller_probability_label_widget.setVisible(True)
            self.generator_settings_controller_probability_widget.setVisible(True)
        else:
            if self.config.distribution == "combination":
                self.generator_settings_controller_probability_label_widget.setVisible(False)
                self.generator_settings_controller_probability_widget.setVisible(False)
            else:
                self.generator_settings_controller_probability_label_widget.setVisible(True)
                self.generator_settings_controller_probability_widget.setVisible(True)
            self.generator_settings_normal_sigma_widget.setVisible(False)
            self.generator_settings_normal_sigma_label_widget.setVisible(False)

    def on_generator_settings_normal_sigma_changed(self):
        self.config.sigma = self.generator_settings_normal_sigma_widget.value()

    def generate_poses(self):
        frame_num = self.config.num_samples
        start_frame = self.config.start_frame
        gauss = self.config.distribution == 'normal'
        gauss_sigma = self.config.sigma
        combination = self.config.distribution == 'combination'
        prob = self.config.controller_probability * 0.01
        channels = self.config.channels
        channel_num = len(channels)
        if channel_num < 1 or prob < 1.0e-7:
            return

        # 根据配置计算一下总帧数 * channel 数
        generate_frame_num = frame_num
        total_operator_num = generate_frame_num + channel_num
        if combination:
            generate_frame_num = int(np.prod(np.array([channels[c_idx].sample_num for c_idx in range(0, channel_num)], dtype=int)))
            total_operator_num = generate_frame_num + channel_num
        self.process_bar.start_progress_bar('Generating...', True, total_operator_num)

        # 数据生成
        key_times = om.MTimeArray()
        channel_values = np.empty((generate_frame_num, channel_num), dtype=float)
        # 组合
        if combination:
            # 设置时间线
            end_frame = start_frame + generate_frame_num
            cmds.playbackOptions(minTime=0, maxTime=end_frame)

            # 插值生成
            channels_value_array = []
            channels_index_array = [] # 用于标识当前值索引
            for i in range(channel_num):
                channel_i_value_array = []
                channel_info = channels[i]
                if channel_info.sample_num == 1:
                    channel_i_value_array.append((channel_info.max_value + channel_info.min_value) * 0.5)
                else:
                    step_value = (channel_info.max_value - channel_info.min_value) / (channel_info.sample_num - 1)
                    for j in range(0, channel_info.sample_num):
                        channel_i_value_array.append(channel_info.min_value + step_value * j)
                channels_value_array.append(channel_i_value_array)
                channels_index_array.append(0)

            # 取消节点
            if self.process_bar.is_progress_bar_cancelled():
                return

            # 生成通道值
            for i in range(generate_frame_num):
                key_times.append(om.MTime(i + start_frame))
            # 生成所有组合
            combinations = itertools.product(*channels_value_array)
            # 填充 channel_values 数组
            for idx, combination in enumerate(combinations):
                channel_values[idx, :] = combination
        # 随机
        else:
            # 设置时间线
            end_frame = start_frame + frame_num
            cmds.playbackOptions(minTime=0, maxTime=end_frame)

            # 生成组字典 {group_name, [int]}，用于设置是否随机
            group_dict = dict()
            for i in range(channel_num):
                group_name = channels[i].group_name
                if group_dict.__contains__(group_name):
                    group_dict[group_name].append(i)
                else:
                    group_dict[group_name] = [i]
            group_num = len(group_dict)
            random_sign = [True for x in range(channel_num)]

            # 取消节点
            if self.process_bar.is_progress_bar_cancelled():
                return

            # 随机数参数
            gauss_centre = None
            gauss_width = None
            if gauss:
                gauss_centre_iter = ((channels[c_idx].max_value + channels[c_idx].min_value) * 0.5 for c_idx in range(channel_num))
                gauss_centre = np.fromiter(gauss_centre_iter, dtype=float)
                gauss_width_iter = (abs(channels[c_idx].max_value - channels[c_idx].min_value) * gauss_sigma for c_idx in range(channel_num))
                gauss_width = np.fromiter(gauss_width_iter, dtype=float)
            uniform_low_iter = (channels[c_idx].min_value for c_idx in range(channel_num))
            uniform_low = np.fromiter(uniform_low_iter, dtype=float)
            uniform_high_iter = (channels[c_idx].max_value for c_idx in range(channel_num))
            uniform_high = np.fromiter(uniform_high_iter, dtype=float)

            # 取消节点
            if self.process_bar.is_progress_bar_cancelled():
                return

            # 生成通道值
            for i in range(frame_num):
                key_times.append(om.MTime(i + start_frame))
                # 首先确定这一帧有哪些组随机，哪些通道用默认的
                if prob < 0.999:
                    for key, value in group_dict.items():
                        random_value = random.uniform(0.0, 1.0)
                        if random_value < prob:
                            for c_idx in value:
                                random_sign[c_idx] = True
                        else:
                            for c_idx in value:
                                random_sign[c_idx] = False
                # 设置通道值到数组
                for j in range(channel_num):
                    if random_sign[j]:
                        if gauss:
                            random_value = np.random.normal(gauss_centre[j], gauss_width[j])
                            while not(uniform_low[j] <= random_value <= uniform_high[j]):
                                random_value = np.random.normal(gauss_centre[j], gauss_width[j])
                            channel_values[i][j] = random_value
                        else:
                            channel_values[i][j] = np.random.uniform(uniform_low[j], uniform_high[j])
                    else:
                        channel_values[i][j] = channels[j].default_value
                # 更新进度条
                self.process_bar.set_progress_bar_value(i)

        # 取消节点
        if self.process_bar.is_progress_bar_cancelled():
            return

        # 将生成的数据作为曲线应用到maya
        for c_idx in range(channel_num):
            ctrl, attr = channels[c_idx].display_name.split('.')
            key_values_list = channel_values[:, c_idx].tolist()
            set_keyframes(ctrl, attr, key_times, key_values_list)
            self.process_bar.set_progress_bar_value(c_idx + generate_frame_num)
            # 取消节点
            if self.process_bar.is_progress_bar_cancelled():
                return

        # 数据生成结束
        self.process_bar.stop_progress_bar()

