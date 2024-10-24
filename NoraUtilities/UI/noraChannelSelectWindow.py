# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraChannelSelectWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_noraChannelSelectWindow(object):
    def setupUi(self, noraChannelSelectWindow):
        if not noraChannelSelectWindow.objectName():
            noraChannelSelectWindow.setObjectName(u"noraChannelSelectWindow")
        noraChannelSelectWindow.resize(327, 490)
        noraChannelSelectWindow.setStyleSheet(u"font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.mainWidget = QWidget(noraChannelSelectWindow)
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
        self.listWidget = QListWidget(self.groupBox)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_2.addWidget(self.listWidget)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(noraChannelSelectWindow)

        QMetaObject.connectSlotsByName(noraChannelSelectWindow)
    # setupUi

    def retranslateUi(self, noraChannelSelectWindow):
        noraChannelSelectWindow.setWindowTitle(QCoreApplication.translate("noraChannelSelectWindow", u"Dialog", None))
        self.groupBox.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("noraChannelSelectWindow", u"\u6dfb\u52a0\u9009\u4e2d\u5bf9\u8c61\u7684 Channels", None))
    # retranslateUi

