# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraPoseGenSettingsWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_noraPoseGenSettingsWindow(object):
    def setupUi(self, noraPoseGenSettingsWindow):
        if not noraPoseGenSettingsWindow.objectName():
            noraPoseGenSettingsWindow.setObjectName(u"noraPoseGenSettingsWindow")
        noraPoseGenSettingsWindow.resize(321, 482)
        noraPoseGenSettingsWindow.setStyleSheet(u"font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.mainWidget = QWidget(noraPoseGenSettingsWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        self.mainWidget.setGeometry(QRect(0, 0, 321, 481))
        self.verticalLayout = QVBoxLayout(self.mainWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.groupBox = QGroupBox(self.mainWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.tableWidget = QTableWidget(self.groupBox)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.addButton = QPushButton(self.groupBox)
        self.addButton.setObjectName(u"addButton")

        self.verticalLayout_2.addWidget(self.addButton)

        self.saveButton = QPushButton(self.groupBox)
        self.saveButton.setObjectName(u"saveButton")

        self.verticalLayout_2.addWidget(self.saveButton)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(noraPoseGenSettingsWindow)

        QMetaObject.connectSlotsByName(noraPoseGenSettingsWindow)
    # setupUi

    def retranslateUi(self, noraPoseGenSettingsWindow):
        noraPoseGenSettingsWindow.setWindowTitle(QCoreApplication.translate("noraPoseGenSettingsWindow", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("noraPoseGenSettingsWindow", u"Default Min-Max Settings", None))
        self.addButton.setText(QCoreApplication.translate("noraPoseGenSettingsWindow", u"\u6dfb\u52a0", None))
        self.saveButton.setText(QCoreApplication.translate("noraPoseGenSettingsWindow", u"\u4fdd\u5b58", None))
    # retranslateUi

