# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraSSDRWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
    QGroupBox, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_noraSSDRWidget(object):
    def setupUi(self, noraSSDRWidget):
        if not noraSSDRWidget.objectName():
            noraSSDRWidget.setObjectName(u"noraSSDRWidget")
        noraSSDRWidget.resize(419, 553)
        self.verticalLayout_4 = QVBoxLayout(noraSSDRWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.targetsGroupBox = QGroupBox(noraSSDRWidget)
        self.targetsGroupBox.setObjectName(u"targetsGroupBox")
        self.verticalLayout = QVBoxLayout(self.targetsGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.targetsVerticalLayout = QVBoxLayout()
        self.targetsVerticalLayout.setObjectName(u"targetsVerticalLayout")

        self.verticalLayout.addLayout(self.targetsVerticalLayout)


        self.verticalLayout_4.addWidget(self.targetsGroupBox)

        self.settingsGroupBox = QGroupBox(noraSSDRWidget)
        self.settingsGroupBox.setObjectName(u"settingsGroupBox")
        self.verticalLayout_2 = QVBoxLayout(self.settingsGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.settingsVerticalLayout = QVBoxLayout()
        self.settingsVerticalLayout.setObjectName(u"settingsVerticalLayout")

        self.verticalLayout_2.addLayout(self.settingsVerticalLayout)

        self.line = QFrame(self.settingsGroupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.settingsVerticalLayout2 = QVBoxLayout()
        self.settingsVerticalLayout2.setObjectName(u"settingsVerticalLayout2")

        self.verticalLayout_2.addLayout(self.settingsVerticalLayout2)

        self.line_2 = QFrame(self.settingsGroupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.settingsVerticalLayout3 = QVBoxLayout()
        self.settingsVerticalLayout3.setObjectName(u"settingsVerticalLayout3")
        self.laplacianCheckBox = QCheckBox(self.settingsGroupBox)
        self.laplacianCheckBox.setObjectName(u"laplacianCheckBox")
        self.laplacianCheckBox.setStyleSheet(u"QCheckBox {\n"
"    color:#eff0f1;\n"
"}")

        self.settingsVerticalLayout3.addWidget(self.laplacianCheckBox)


        self.verticalLayout_2.addLayout(self.settingsVerticalLayout3)

        self.secondaryModeCheckBox = QCheckBox(self.settingsGroupBox)
        self.secondaryModeCheckBox.setObjectName(u"secondaryModeCheckBox")
        self.secondaryModeCheckBox.setStyleSheet(u"QCheckBox {\n"
"    color:#eff0f1;\n"
"}")

        self.verticalLayout_2.addWidget(self.secondaryModeCheckBox)


        self.verticalLayout_4.addWidget(self.settingsGroupBox)

        self.groupBox = QGroupBox(noraSSDRWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.GenerateJointsAndWeightPushButton = QPushButton(self.groupBox)
        self.GenerateJointsAndWeightPushButton.setObjectName(u"GenerateJointsAndWeightPushButton")

        self.verticalLayout_3.addWidget(self.GenerateJointsAndWeightPushButton)


        self.verticalLayout_4.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.retranslateUi(noraSSDRWidget)

        QMetaObject.connectSlotsByName(noraSSDRWidget)
    # setupUi

    def retranslateUi(self, noraSSDRWidget):
        noraSSDRWidget.setWindowTitle(QCoreApplication.translate("noraSSDRWidget", u"Dialog", None))
        self.targetsGroupBox.setTitle(QCoreApplication.translate("noraSSDRWidget", u"Targets", None))
        self.settingsGroupBox.setTitle(QCoreApplication.translate("noraSSDRWidget", u"Settings", None))
        self.laplacianCheckBox.setText(QCoreApplication.translate("noraSSDRWidget", u"\u5e73\u6ed1\u6743\u91cd", None))
        self.secondaryModeCheckBox.setText(QCoreApplication.translate("noraSSDRWidget", u"\u6b21\u7ea7\u9aa8\u9abc\u6a21\u5f0f", None))
        self.groupBox.setTitle(QCoreApplication.translate("noraSSDRWidget", u"Actions", None))
        self.GenerateJointsAndWeightPushButton.setText(QCoreApplication.translate("noraSSDRWidget", u"\u751f\u6210\u9aa8\u9abc\u548c\u6743\u91cd\u4fe1\u606f", None))
    # retranslateUi

