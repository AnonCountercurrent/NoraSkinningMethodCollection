# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraLabelWidget.ui'
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
    QSizePolicy, QWidget)

class Ui_noraLabelLayout(object):
    def setupUi(self, noraLabelLayout):
        if not noraLabelLayout.objectName():
            noraLabelLayout.setObjectName(u"noraLabelLayout")
        noraLabelLayout.resize(400, 300)
        self.horizontalLayoutWidget = QWidget(noraLabelLayout)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 10, 160, 41))
        self.labelLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.labelLayout.setObjectName(u"labelLayout")
        self.labelLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.labelLayout.addWidget(self.label)


        self.retranslateUi(noraLabelLayout)

        QMetaObject.connectSlotsByName(noraLabelLayout)
    # setupUi

    def retranslateUi(self, noraLabelLayout):
        noraLabelLayout.setWindowTitle(QCoreApplication.translate("noraLabelLayout", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("noraLabelLayout", u"TextLabel", None))
    # retranslateUi

