import os
import sys
import importlib
from importlib import reload
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
from NoraUI import noraMainWindow
from NoraUI.noraMainWindow import Ui_noraMainWindow
from NoraGeneral.noraUtilities import *

reload(noraMainWindow)


class NoraMain(QtWidgets.QDialog, Ui_noraMainWindow):
    def __init__(self, parent=None):
        super(NoraMain, self).__init__()
        self.setObjectName("noraSMCWin")
        self.setParent(get_maya_main_window())
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowTitle("Nora Skinning Method Collection")
        self.setWindowIcon(QtGui.QIcon(get_icon_path("Nora_Valkyrie_Emblem_128.png")))

        # 添加ui
        self.tabWidget = QTabWidget(self.mainWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.mainLayout.addWidget(self.tabWidget)

        # 选项卡字典
        self.tab_map = {}
        self.module_map = {}
        self.create_ui()

    def create_ui(self):
        current_path = __file__
        current_path = os.path.dirname(current_path)
        modules = os.listdir(current_path)
        modules = [item for item in modules if '.' not in item]

        # 读取模块的顺序
        # 读取order.txt
        module_order_list = []
        order_file = current_path + '/order.txt'
        order_data = open(order_file, 'r')
        module_order_list.extend(order_data.read().splitlines())
        order_data.close()
        # 录入模块名路径
        for tab in modules:
            self.tab_map[tab] = current_path + '/' + tab
        # 樣式
        widget_types = ['QLabel', 'QCheckBox', 'QPushButton', 'QLineEdit', 'QListWidget',
                        'QComboBox', 'QGroupBox', 'QRadioButton', 'QDoubleSpinBox', 'QSpinBox']
        style_sheet_str = 'font: 9pt "微软雅黑";'
        for w in widget_types:
            style_sheet_str += w + '{color:#eff0f1}'
            style_sheet_str += w + ':disabled{color:#777777;background-color:#494949;}'
        style_sheet_str += 'QPushButton{background-color:#3e3e3e}'
        # 遍历模块列表
        for tab in module_order_list:
            if self.tab_map.__contains__(tab):
                key = tab
                value = self.tab_map[key]
                # 获取模块文件夹下的文件
                tool_modules = os.listdir(value)

                # split .py .pyc
                tool_modules = list(set([item.split('.')[0] for item in tool_modules]))
                # store tab&modules
                self.module_map[key] = tool_modules

                # 读取order.txt
                order_list = []
                order_file = value + '/order.txt'
                order_data = open(order_file, 'r')
                order_list.extend(order_data.read().splitlines())
                order_data.close()

                # create toolBox
                tool_box = QtWidgets.QToolBox()
                tool_box.setLayoutDirection(QtCore.Qt.LeftToRight)
                tool_box.setFrameShape(QtWidgets.QFrame.StyledPanel)
                tool_box.layout().setSpacing(3)

                module_num = 0
                # 读取order.txt中的模块
                if value not in sys.path:
                    sys.path.append(value)
                for module in order_list:
                    if module in tool_modules:
                        tool_modules.remove(module)
                        the_module = importlib.import_module(module)
                        reload(the_module)

                        widget = the_module.get_ui()
                        widget.resize(the_module.get_width(), the_module.get_height())
                        widget.setMinimumWidth(the_module.get_width())
                        widget.setMinimumHeight(the_module.get_height())
                        if not the_module.get_use_custom_front_style():
                            widget.setStyleSheet(style_sheet_str)
                        tool_box.addItem(widget, the_module.get_title())
                        module_num += 1

                tool_box.setCurrentIndex(0)
                # add tab
                tab_display_name = key.replace("Nora", "")
                self.tabWidget.addTab(tool_box, tab_display_name)
