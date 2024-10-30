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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGroupBox, QHBoxLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_noraPolynomialFittingWidget(object):
    def setupUi(self, noraPolynomialFittingWidget):
        if not noraPolynomialFittingWidget.objectName():
            noraPolynomialFittingWidget.setObjectName(u"noraPolynomialFittingWidget")
        noraPolynomialFittingWidget.resize(617, 580)
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
        self.radiansCheckBox = QCheckBox(self.settingsGroupBox)
        self.radiansCheckBox.setObjectName(u"radiansCheckBox")
        self.radiansCheckBox.setStyleSheet(u"QCheckBox {\n"
"    color:#eff0f1;\n"
"}")
        self.radiansCheckBox.setChecked(True)

        self.driverLayout.addWidget(self.radiansCheckBox)

        self.csvCheckBox = QCheckBox(self.settingsGroupBox)
        self.csvCheckBox.setObjectName(u"csvCheckBox")
        self.csvCheckBox.setStyleSheet(u"QCheckBox {\n"
"    color:#eff0f1;\n"
"}")
        self.csvCheckBox.setChecked(False)

        self.driverLayout.addWidget(self.csvCheckBox)

        self.printCheckBox = QCheckBox(self.settingsGroupBox)
        self.printCheckBox.setObjectName(u"printCheckBox")
        self.printCheckBox.setStyleSheet(u"QCheckBox {\n"
"    color:#eff0f1;\n"
"}")
        self.printCheckBox.setChecked(False)

        self.driverLayout.addWidget(self.printCheckBox)

        self.genDriverNodeCheckBox = QCheckBox(self.settingsGroupBox)
        self.genDriverNodeCheckBox.setObjectName(u"genDriverNodeCheckBox")
        self.genDriverNodeCheckBox.setStyleSheet(u"QCheckBox {\n"
"    color:#eff0f1;\n"
"}")
        self.genDriverNodeCheckBox.setChecked(True)

        self.driverLayout.addWidget(self.genDriverNodeCheckBox)


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
        self.radiansCheckBox.setText(QCoreApplication.translate("noraPolynomialFittingWidget", u"\u65cb\u8f6c\u901a\u9053\u503c\u4f7f\u7528\u5f27\u5ea6", None))
        self.csvCheckBox.setText(QCoreApplication.translate("noraPolynomialFittingWidget", u"\u751f\u6210\u9a71\u52a8\u6570\u636e\u8868\u5230\u6587\u6863", None))
        self.printCheckBox.setText(QCoreApplication.translate("noraPolynomialFittingWidget", u"\u6253\u5370\u53c2\u6570", None))
        self.genDriverNodeCheckBox.setText(QCoreApplication.translate("noraPolynomialFittingWidget", u"\u751f\u6210\u9a71\u52a8\u8282\u70b9", None))
        self.groupBox.setTitle(QCoreApplication.translate("noraPolynomialFittingWidget", u"Actions", None))
        self.generateButton.setText(QCoreApplication.translate("noraPolynomialFittingWidget", u"\u751f\u6210\u9a71\u52a8\u4fe1\u606f", None))
    # retranslateUi

