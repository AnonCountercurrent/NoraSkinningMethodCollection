# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraPoseGeneratorWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_noraPoseGeneratorWidget(object):
    def setupUi(self, noraPoseGeneratorWidget):
        if not noraPoseGeneratorWidget.objectName():
            noraPoseGeneratorWidget.setObjectName(u"noraPoseGeneratorWidget")
        noraPoseGeneratorWidget.resize(400, 95)
        self.verticalLayout_2 = QVBoxLayout(noraPoseGeneratorWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(noraPoseGeneratorWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.openPoseGenerator = QPushButton(self.groupBox)
        self.openPoseGenerator.setObjectName(u"openPoseGenerator")

        self.verticalLayout.addWidget(self.openPoseGenerator)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 136, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(noraPoseGeneratorWidget)

        QMetaObject.connectSlotsByName(noraPoseGeneratorWidget)
    # setupUi

    def retranslateUi(self, noraPoseGeneratorWidget):
        noraPoseGeneratorWidget.setWindowTitle(QCoreApplication.translate("noraPoseGeneratorWidget", u"Dialog", None))
        self.groupBox.setTitle("")
        self.openPoseGenerator.setText(QCoreApplication.translate("noraPoseGeneratorWidget", u"\u6253\u5f00\u5e27\u751f\u6210\u5668", None))
    # retranslateUi

