# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraLoadDriverConfigWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_noraLoadDriverConfigDialog(object):
    def setupUi(self, noraLoadDriverConfigDialog):
        if not noraLoadDriverConfigDialog.objectName():
            noraLoadDriverConfigDialog.setObjectName(u"noraLoadDriverConfigDialog")
        noraLoadDriverConfigDialog.resize(519, 366)
        self.verticalLayoutWidget = QWidget(noraLoadDriverConfigDialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 10, 411, 43))
        self.loadDriverConfigLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.loadDriverConfigLayout.setObjectName(u"loadDriverConfigLayout")
        self.loadDriverConfigLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.loadDriverConfigLayout.addWidget(self.label)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.loadDriverConfigLayout.addWidget(self.pushButton)


        self.retranslateUi(noraLoadDriverConfigDialog)

        QMetaObject.connectSlotsByName(noraLoadDriverConfigDialog)
    # setupUi

    def retranslateUi(self, noraLoadDriverConfigDialog):
        noraLoadDriverConfigDialog.setWindowTitle(QCoreApplication.translate("noraLoadDriverConfigDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("noraLoadDriverConfigDialog", u"Driver Info: None", None))
        self.pushButton.setText(QCoreApplication.translate("noraLoadDriverConfigDialog", u"\u52a0\u8f7d\u9a71\u52a8\u914d\u7f6e", None))
    # retranslateUi

