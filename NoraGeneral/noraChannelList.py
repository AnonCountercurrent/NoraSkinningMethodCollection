from importlib import reload
from PySide6 import QtGui
from NoraGeneral.UI import noraListWidget
from NoraUtilities.UI import noraChannelSelectWindow
from NoraGeneral import noraLabel
from NoraGeneral.noraUtilities import *
from dataclasses import dataclass

reload(noraListWidget)
reload(noraChannelSelectWindow)
reload(noraLabel)


@dataclass
class ChannelName:
    name: str
    display_name: str
    channel_name: str
    obj_name: str


class NoraGeneralChannelSelectWindow(QtWidgets.QMainWindow, noraChannelSelectWindow.Ui_noraChannelSelectWindow):
    def __init__(self, parent, duplicate_check_map: dict, add_fun):
        super(NoraGeneralChannelSelectWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Add Channels 2')
        self.setObjectName("noraAddChannelsWin2")
        self.setWindowIcon(QtGui.QIcon(get_icon_path("Nora_Valkyrie_Emblem_128.png")))
        self.setCentralWidget(self.mainWidget)
        self.pushButton.clicked.connect(self.add_channels)

        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        self.duplicate_check_map = duplicate_check_map
        self.generator = parent
        self.selected_objects = None
        self.current_channels = list() #(channel_name, full_path_name, short_name)
        self.add_fun = add_fun

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
                    if self.duplicate_check_map.__contains__(full_path_name):
                        continue
                    # 添加到当前Channel列表
                    channel_info = ChannelName(full_path_name, get_short_name(obj) + '.' + long_channel_name, long_channel_name, obj)
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
        # 回调
        self.add_fun(channels_to_add)

        # 关闭自己
        self.close()

class NoraChannelList(QtWidgets.QDialog, noraListWidget.Ui_noraListDialog):
    def __init__(self, parent=None):
        super(NoraChannelList, self).__init__(parent)
        self.setParent(parent)
        self.setupUi(self)
        self.setLayout(self.noraChannelListLayout)

        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        # 成员
        self.add_channels_win = None

        # 事件
        self.addButton.clicked.connect(self.add_button_clicked)
        self.removeButton.clicked.connect(self.remove_button_clicked)
        self.selectButton.clicked.connect(self.select_button_clicked)

    def add_button_clicked(self):
        # 收集当前列表里的Channel到dict
        temp_channel_map = {}
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            item_widget = self.listWidget.itemWidget(item)
            temp_channel_map[item_widget.info] = 1
        # 弹出Channel选择窗体
        if cmds.window('noraAddChannelsWin2', ex=True):
            cmds.deleteUI('noraAddChannelsWin2')
        self.add_channels_win = NoraGeneralChannelSelectWindow(self, temp_channel_map, self.add_fun)
        self.add_channels_win.show()

    def remove_button_clicked(self):
        items = self.listWidget.selectedItems()
        for item in items:
            row = self.listWidget.row(item)
            self.listWidget.takeItem(row)

    def select_button_clicked(self):
        items = self.listWidget.selectedItems()
        select_list = []
        for item in items:
            item_widget = self.listWidget.itemWidget(item)
            if not any(item_widget.info2 == x for x in select_list):
                select_list.append(item_widget.info2)
        if len(select_list) > 0:
            cmds.select(select_list)

    def add_fun(self, add_list):
        for item in add_list:
            label_item = noraLabel.NoraLabel()
            label_item.set_label_text(item.display_name)
            label_item.info = item.name
            label_item.info2 = item.obj_name
            list_item = QtWidgets.QListWidgetItem(self.listWidget)
            list_item.listWidget()
            list_item.setSizeHint(label_item.minimumSizeHint())
            self.listWidget.setItemWidget(list_item, label_item)