# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraModelSelectWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_noraModelSelectedWidget(object):
    def setupUi(self, noraModelSelectedWidget):
        if not noraModelSelectedWidget.objectName():
            noraModelSelectedWidget.setObjectName(u"noraModelSelectedWidget")
        noraModelSelectedWidget.resize(650, 308)
        noraModelSelectedWidget.setStyleSheet(u"")
        self.verticalLayoutWidget = QWidget(noraModelSelectedWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 541, 111))
        self.modelSelectWithFrameRangeLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.modelSelectWithFrameRangeLayout.setObjectName(u"modelSelectWithFrameRangeLayout")
        self.modelSelectWithFrameRangeLayout.setContentsMargins(0, 0, 0, 0)
        self.modelSelectLayout = QVBoxLayout()
        self.modelSelectLayout.setObjectName(u"modelSelectLayout")

        self.modelSelectWithFrameRangeLayout.addLayout(self.modelSelectLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.leftRange = QLineEdit(self.verticalLayoutWidget)
        self.leftRange.setObjectName(u"leftRange")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftRange.sizePolicy().hasHeightForWidth())
        self.leftRange.setSizePolicy(sizePolicy1)
        self.leftRange.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_3.addWidget(self.leftRange)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.rightRange = QLineEdit(self.verticalLayoutWidget)
        self.rightRange.setObjectName(u"rightRange")
        sizePolicy1.setHeightForWidth(self.rightRange.sizePolicy().hasHeightForWidth())
        self.rightRange.setSizePolicy(sizePolicy1)
        self.rightRange.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_3.addWidget(self.rightRange)


        self.modelSelectWithFrameRangeLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(noraModelSelectedWidget)

        QMetaObject.connectSlotsByName(noraModelSelectedWidget)
    # setupUi

    def retranslateUi(self, noraModelSelectedWidget):
        noraModelSelectedWidget.setWindowTitle(QCoreApplication.translate("noraModelSelectedWidget", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("noraModelSelectedWidget", u"\u5e27\u6570\u533a\u95f4\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("noraModelSelectedWidget", u"-", None))
    # retranslateUi

