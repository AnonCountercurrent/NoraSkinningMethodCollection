# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraJointSettingsWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_noraJointSettingsWidget(object):
    def setupUi(self, noraJointSettingsWidget):
        if not noraJointSettingsWidget.objectName():
            noraJointSettingsWidget.setObjectName(u"noraJointSettingsWidget")
        noraJointSettingsWidget.resize(422, 324)
        self.verticalLayout_3 = QVBoxLayout(noraJointSettingsWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(noraJointSettingsWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.makeJointScaledUEStylePushButton = QPushButton(self.groupBox)
        self.makeJointScaledUEStylePushButton.setObjectName(u"makeJointScaledUEStylePushButton")

        self.verticalLayout.addWidget(self.makeJointScaledUEStylePushButton)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(noraJointSettingsWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.rideVerticalLayout = QVBoxLayout()
        self.rideVerticalLayout.setObjectName(u"rideVerticalLayout")

        self.verticalLayout_2.addLayout(self.rideVerticalLayout)

        self.restBipPushButton = QPushButton(self.groupBox_2)
        self.restBipPushButton.setObjectName(u"restBipPushButton")

        self.verticalLayout_2.addWidget(self.restBipPushButton)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 254, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.retranslateUi(noraJointSettingsWidget)

        QMetaObject.connectSlotsByName(noraJointSettingsWidget)
    # setupUi

    def retranslateUi(self, noraJointSettingsWidget):
        noraJointSettingsWidget.setWindowTitle(QCoreApplication.translate("noraJointSettingsWidget", u"Dialog", None))
        self.groupBox.setTitle("")
        self.makeJointScaledUEStylePushButton.setText(QCoreApplication.translate("noraJointSettingsWidget", u"\u8bbe\u7f6e\u9009\u4e2d\u9aa8\u9abc\u4f7f\u7528UE\u98ce\u683c\u7684\u7f29\u653e", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("noraJointSettingsWidget", u"Reset transform", None))
        self.restBipPushButton.setText(QCoreApplication.translate("noraJointSettingsWidget", u"\u5c06Bip001\u8bbe\u7f6e\u5230\u539f\u70b9", None))
    # retranslateUi

