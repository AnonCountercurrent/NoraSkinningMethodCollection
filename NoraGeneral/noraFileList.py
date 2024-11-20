from importlib import reload
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QAbstractItemView
import urllib, os
from NoraGeneral.UI import noraFileListWidget
from NoraGeneral.noraUtilities import *

reload(noraFileListWidget)

class NoraDropEnabledListWidget(QtWidgets.QListWidget):
    fileDropped = QtCore.Signal(list)
    def __init__(self, parent=None):
        super(NoraDropEnabledListWidget, self).__init__(parent)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.setDropIndicatorShown(True)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(urllib.request.unquote(url.toLocalFile()))
            self.fileDropped.emit(links)
        else:
            event.ignore()

    def is_string_exist(self, in_str):
        item_num = self.count()
        if any(in_str == self.item(item_idx).text() for item_idx in range(item_num)):
            return True
        return False


class NoraFileList(QtWidgets.QDialog, noraFileListWidget.Ui_noraFilePathListDialog):
    typeDict = {'mb': 'mayaBinary', 'ma': 'mayaAscii', 'fbx': 'FBX', 'FBX': 'FBX'}
    optionsDict = {'mb': 'v=0;', 'ma': 'v=0;', 'fbx': 'fbx', 'FBX': 'fbx'}
    def __init__(self, parent=None):
        super(NoraFileList, self).__init__(parent)
        self.setParent(parent)
        self.setupUi(self)
        self.setLayout(self.fileListVerticalLayout)
        self.listWidget = NoraDropEnabledListWidget()
        self.listVerticalLayout.addWidget(self.listWidget)
        # var
        self.file_only = True
        self.path_only = False
        # button's icon
        self.open_icon = self.style().standardIcon(getattr(QtWidgets.QStyle, "SP_DialogOpenButton"))
        self.addPushButton.setIcon(self.open_icon)
        self.remove_icon = self.style().standardIcon(getattr(QtWidgets.QStyle, "SP_DialogCancelButton"))
        self.removePushButton.setIcon(self.remove_icon)
        self.clear_icon = self.style().standardIcon(getattr(QtWidgets.QStyle, "SP_DialogResetButton"))
        self.clearPushButton.setIcon(self.clear_icon)
        # events
        self.listWidget.fileDropped.connect(self.file_dropped)
        self.addPushButton.clicked.connect(self.add_item)
        self.removePushButton.clicked.connect(self.remove_selected_item)
        self.clearPushButton.clicked.connect(self.clear_list)

    def file_dropped(self, links):
        for url in links:
            if os.path.exists(url) and not self.listWidget.is_string_exist(url):
                if self.file_only:
                    if os.path.isfile(url):
                        self.listWidget.addItem(url)
                elif self.path_only:
                    if os.path.isdir(url):
                        self.listWidget.addItem(url)
                else:
                    self.listWidget.addItem(url)

    def add_item(self):
        paths = []
        if self.file_only:
            paths, _ = QtWidgets.QFileDialog.getOpenFileNames(
                parent=self,
                caption='选择文件',
                dir=get_document_path())
        elif self.path_only:
            path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Path', get_document_path(), QtWidgets.QFileDialog.ShowDirsOnly)
            if path is not None:
                paths.append(path)
        if paths is not None:
            for path in paths:
                if not self.listWidget.is_string_exist(path):
                    self.listWidget.addItem(path)

    def remove_selected_item(self):
        items = self.listWidget.selectedItems()
        for item in items:
            row = self.listWidget.row(item)
            self.listWidget.takeItem(row)

    def clear_list(self):
        self.listWidget.clear()

    def get_file_list(self):
        file_list = []
        for item_idx in range(self.listWidget.count()):
            item = self.listWidget.item(item_idx)
            file_list.append(item.text())
        return file_list
