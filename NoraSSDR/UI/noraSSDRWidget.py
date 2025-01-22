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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_noraSSDRWidget(object):
    def setupUi(self, noraSSDRWidget):
        if not noraSSDRWidget.objectName():
            noraSSDRWidget.setObjectName(u"noraSSDRWidget")
        noraSSDRWidget.resize(504, 399)
        self.verticalLayout = QVBoxLayout(noraSSDRWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(noraSSDRWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 461, 51))
        self.targetsVerticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.targetsVerticalLayout.setObjectName(u"targetsVerticalLayout")
        self.targetsVerticalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 360, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(noraSSDRWidget)

        QMetaObject.connectSlotsByName(noraSSDRWidget)
    # setupUi

    def retranslateUi(self, noraSSDRWidget):
        noraSSDRWidget.setWindowTitle(QCoreApplication.translate("noraSSDRWidget", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("noraSSDRWidget", u"Base", None))
    # retranslateUi

