# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraIntNumberWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QSizePolicy, QSpinBox, QWidget)

class Ui_intNumberLayoutDialog(object):
    def setupUi(self, intNumberLayoutDialog):
        if not intNumberLayoutDialog.objectName():
            intNumberLayoutDialog.setObjectName(u"intNumberLayoutDialog")
        intNumberLayoutDialog.resize(461, 351)
        self.layoutWidget = QWidget(intNumberLayoutDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 80, 246, 22))
        self.intNumberLayout = QHBoxLayout(self.layoutWidget)
        self.intNumberLayout.setObjectName(u"intNumberLayout")
        self.intNumberLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.intNumberLayout.addWidget(self.label)

        self.intNumber = QSpinBox(self.layoutWidget)
        self.intNumber.setObjectName(u"intNumber")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.intNumber.sizePolicy().hasHeightForWidth())
        self.intNumber.setSizePolicy(sizePolicy1)
        self.intNumber.setMinimumSize(QSize(80, 0))
        self.intNumber.setMaximum(1000000000)

        self.intNumberLayout.addWidget(self.intNumber)


        self.retranslateUi(intNumberLayoutDialog)

        QMetaObject.connectSlotsByName(intNumberLayoutDialog)
    # setupUi

    def retranslateUi(self, intNumberLayoutDialog):
        intNumberLayoutDialog.setWindowTitle(QCoreApplication.translate("intNumberLayoutDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("intNumberLayoutDialog", u"Lable\uff1a", None))
    # retranslateUi

