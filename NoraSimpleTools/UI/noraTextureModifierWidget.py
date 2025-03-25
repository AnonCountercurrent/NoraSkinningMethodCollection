# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraTextureModifierWidget.ui'
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
    QGroupBox, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_noraTextureModifierWidget(object):
    def setupUi(self, noraTextureModifierWidget):
        if not noraTextureModifierWidget.objectName():
            noraTextureModifierWidget.setObjectName(u"noraTextureModifierWidget")
        noraTextureModifierWidget.resize(502, 493)
        self.verticalLayout_2 = QVBoxLayout(noraTextureModifierWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(noraTextureModifierWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.texMapTargetslLayout = QVBoxLayout()
        self.texMapTargetslLayout.setObjectName(u"texMapTargetslLayout")

        self.verticalLayout.addLayout(self.texMapTargetslLayout)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.texMapSettingslLayout = QVBoxLayout()
        self.texMapSettingslLayout.setObjectName(u"texMapSettingslLayout")

        self.verticalLayout.addLayout(self.texMapSettingslLayout)

        self.normalCheckBox = QCheckBox(self.groupBox)
        self.normalCheckBox.setObjectName(u"normalCheckBox")

        self.verticalLayout.addWidget(self.normalCheckBox)

        self.originTangentCheckBox = QCheckBox(self.groupBox)
        self.originTangentCheckBox.setObjectName(u"originTangentCheckBox")
        self.originTangentCheckBox.setEnabled(True)
        self.originTangentCheckBox.setChecked(True)

        self.verticalLayout.addWidget(self.originTangentCheckBox)

        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.mappingPushButton = QPushButton(self.groupBox)
        self.mappingPushButton.setObjectName(u"mappingPushButton")

        self.verticalLayout.addWidget(self.mappingPushButton)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(noraTextureModifierWidget)

        QMetaObject.connectSlotsByName(noraTextureModifierWidget)
    # setupUi

    def retranslateUi(self, noraTextureModifierWidget):
        noraTextureModifierWidget.setWindowTitle(QCoreApplication.translate("noraTextureModifierWidget", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("noraTextureModifierWidget", u"Texture Mapping", None))
        self.normalCheckBox.setText(QCoreApplication.translate("noraTextureModifierWidget", u"\u6cd5\u7ebf\u56fe", None))
        self.originTangentCheckBox.setText(QCoreApplication.translate("noraTextureModifierWidget", u"\u5207\u7ebf\u7a7a\u95f4\u53d8\u6362\u6a21\u5f0f", None))
        self.mappingPushButton.setText(QCoreApplication.translate("noraTextureModifierWidget", u"\u751f\u6210\u7eb9\u7406", None))
    # retranslateUi

