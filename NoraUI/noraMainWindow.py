# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraMainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_noraMainWindow(object):
    def setupUi(self, noraMainWindow):
        if not noraMainWindow.objectName():
            noraMainWindow.setObjectName(u"noraMainWindow")
        noraMainWindow.resize(495, 767)
        noraMainWindow.setWindowTitle(u"NoraSMC")
        noraMainWindow.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(noraMainWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainWidget = QWidget(noraMainWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        self.verticalLayout_3 = QVBoxLayout(self.mainWidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setSpacing(1)
        self.mainLayout.setObjectName(u"mainLayout")

        self.verticalLayout_3.addLayout(self.mainLayout)


        self.verticalLayout.addWidget(self.mainWidget)


        self.retranslateUi(noraMainWindow)

        QMetaObject.connectSlotsByName(noraMainWindow)
    # setupUi

    def retranslateUi(self, noraMainWindow):
        pass
    # retranslateUi

