# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraFrameRangeWidget.ui'
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

class Ui_noraFrameRangeDialog(object):
    def setupUi(self, noraFrameRangeDialog):
        if not noraFrameRangeDialog.objectName():
            noraFrameRangeDialog.setObjectName(u"noraFrameRangeDialog")
        noraFrameRangeDialog.resize(455, 187)
        self.layoutWidget = QWidget(noraFrameRangeDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 30, 246, 22))
        self.frameRangeLayout = QHBoxLayout(self.layoutWidget)
        self.frameRangeLayout.setObjectName(u"frameRangeLayout")
        self.frameRangeLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.frameRangeLayout.addWidget(self.label_3)

        self.leftRange = QSpinBox(self.layoutWidget)
        self.leftRange.setObjectName(u"leftRange")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftRange.sizePolicy().hasHeightForWidth())
        self.leftRange.setSizePolicy(sizePolicy1)
        self.leftRange.setMinimumSize(QSize(80, 0))
        self.leftRange.setMaximum(1000000000)

        self.frameRangeLayout.addWidget(self.leftRange)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)

        self.frameRangeLayout.addWidget(self.label_4)

        self.rightRange = QSpinBox(self.layoutWidget)
        self.rightRange.setObjectName(u"rightRange")
        sizePolicy1.setHeightForWidth(self.rightRange.sizePolicy().hasHeightForWidth())
        self.rightRange.setSizePolicy(sizePolicy1)
        self.rightRange.setMinimumSize(QSize(80, 0))
        self.rightRange.setMaximum(1000000000)
        self.rightRange.setValue(30)

        self.frameRangeLayout.addWidget(self.rightRange)


        self.retranslateUi(noraFrameRangeDialog)

        QMetaObject.connectSlotsByName(noraFrameRangeDialog)
    # setupUi

    def retranslateUi(self, noraFrameRangeDialog):
        noraFrameRangeDialog.setWindowTitle(QCoreApplication.translate("noraFrameRangeDialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("noraFrameRangeDialog", u"\u5e27\u6570\u533a\u95f4\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("noraFrameRangeDialog", u"-", None))
    # retranslateUi

