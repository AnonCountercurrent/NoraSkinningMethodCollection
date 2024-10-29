# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraPolynomialFittingWidget.ui'
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
    QHBoxLayout, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_noraPolynomialFittingWidget(object):
    def setupUi(self, noraPolynomialFittingWidget):
        if not noraPolynomialFittingWidget.objectName():
            noraPolynomialFittingWidget.setObjectName(u"noraPolynomialFittingWidget")
        noraPolynomialFittingWidget.resize(541, 497)
        self.verticalLayout_4 = QVBoxLayout(noraPolynomialFittingWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.baseGroupBox = QGroupBox(noraPolynomialFittingWidget)
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

        self.frameSetLayout = QVBoxLayout()
        self.frameSetLayout.setObjectName(u"frameSetLayout")

        self.verticalLayout.addLayout(self.frameSetLayout)


        self.verticalLayout_4.addWidget(self.baseGroupBox)

        self.settingsGroupBox = QGroupBox(noraPolynomialFittingWidget)
        self.settingsGroupBox.setObjectName(u"settingsGroupBox")
        self.verticalLayout_2 = QVBoxLayout(self.settingsGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.driverLayout = QVBoxLayout()
        self.driverLayout.setObjectName(u"driverLayout")

        self.verticalLayout_2.addLayout(self.driverLayout)


        self.verticalLayout_4.addWidget(self.settingsGroupBox)

        self.groupBox = QGroupBox(noraPolynomialFittingWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.generateButton = QPushButton(self.groupBox)
        self.generateButton.setObjectName(u"generateButton")

        self.verticalLayout_3.addWidget(self.generateButton)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addWidget(self.groupBox)


        self.retranslateUi(noraPolynomialFittingWidget)

        QMetaObject.connectSlotsByName(noraPolynomialFittingWidget)
    # setupUi

    def retranslateUi(self, noraPolynomialFittingWidget):
        noraPolynomialFittingWidget.setWindowTitle(QCoreApplication.translate("noraPolynomialFittingWidget", u"Dialog", None))
        self.baseGroupBox.setTitle(QCoreApplication.translate("noraPolynomialFittingWidget", u"Targets", None))
        self.settingsGroupBox.setTitle(QCoreApplication.translate("noraPolynomialFittingWidget", u"Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("noraPolynomialFittingWidget", u"Actions", None))
        self.generateButton.setText(QCoreApplication.translate("noraPolynomialFittingWidget", u"\u751f\u6210\u9a71\u52a8\u4fe1\u606f", None))
    # retranslateUi

