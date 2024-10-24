# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraFDDAWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGroupBox,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_noraFDDAWidget(object):
    def setupUi(self, noraFDDAWidget):
        if not noraFDDAWidget.objectName():
            noraFDDAWidget.setObjectName(u"noraFDDAWidget")
        noraFDDAWidget.resize(526, 900)
        noraFDDAWidget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(noraFDDAWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.baseGroupBox = QGroupBox(noraFDDAWidget)
        self.baseGroupBox.setObjectName(u"baseGroupBox")
        self.verticalLayout = QVBoxLayout(self.baseGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mdagSelectLayout = QVBoxLayout()
        self.mdagSelectLayout.setObjectName(u"mdagSelectLayout")

        self.verticalLayout.addLayout(self.mdagSelectLayout)

        self.line = QFrame(self.baseGroupBox)
        self.line.setObjectName(u"line")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.mdagSelectLayout2 = QVBoxLayout()
        self.mdagSelectLayout2.setObjectName(u"mdagSelectLayout2")

        self.verticalLayout.addLayout(self.mdagSelectLayout2)


        self.verticalLayout_3.addWidget(self.baseGroupBox)

        self.groupBox = QGroupBox(noraFDDAWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.bindVertexToJoint = QPushButton(self.groupBox)
        self.bindVertexToJoint.setObjectName(u"bindVertexToJoint")
        self.bindVertexToJoint.setMinimumSize(QSize(0, 0))

        self.verticalLayout_2.addWidget(self.bindVertexToJoint)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 326, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.retranslateUi(noraFDDAWidget)

        QMetaObject.connectSlotsByName(noraFDDAWidget)
    # setupUi

    def retranslateUi(self, noraFDDAWidget):
        noraFDDAWidget.setWindowTitle(QCoreApplication.translate("noraFDDAWidget", u"Dialog", None))
        self.baseGroupBox.setTitle(QCoreApplication.translate("noraFDDAWidget", u"Base", None))
        self.groupBox.setTitle(QCoreApplication.translate("noraFDDAWidget", u"Linear Part", None))
        self.bindVertexToJoint.setText(QCoreApplication.translate("noraFDDAWidget", u"\u5c06\u9876\u70b9\u7ed1\u5230\u5bf9\u5176\u53d8\u5f62\u5f71\u54cd\u6700\u5927\u7684\u9aa8\u9abc\u4e0a", None))
    # retranslateUi

