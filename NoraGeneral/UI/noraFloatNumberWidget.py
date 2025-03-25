# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraFloatNumberWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QHBoxLayout,
    QLabel, QSizePolicy, QWidget)

class Ui_noraFloatNumberWidget(object):
    def setupUi(self, noraFloatNumberWidget):
        if not noraFloatNumberWidget.objectName():
            noraFloatNumberWidget.setObjectName(u"noraFloatNumberWidget")
        noraFloatNumberWidget.resize(400, 300)
        self.layoutWidget = QWidget(noraFloatNumberWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(140, 110, 246, 22))
        self.floatNumberLayout = QHBoxLayout(self.layoutWidget)
        self.floatNumberLayout.setObjectName(u"floatNumberLayout")
        self.floatNumberLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.floatNumberLayout.addWidget(self.label)

        self.doubleSpinBox = QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.floatNumberLayout.addWidget(self.doubleSpinBox)


        self.retranslateUi(noraFloatNumberWidget)

        QMetaObject.connectSlotsByName(noraFloatNumberWidget)
    # setupUi

    def retranslateUi(self, noraFloatNumberWidget):
        noraFloatNumberWidget.setWindowTitle(QCoreApplication.translate("noraFloatNumberWidget", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("noraFloatNumberWidget", u"Lable\uff1a", None))
    # retranslateUi

