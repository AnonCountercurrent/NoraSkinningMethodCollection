# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraPathSelectWidget.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_noraPathSelectDialog(object):
    def setupUi(self, noraPathSelectDialog):
        if not noraPathSelectDialog.objectName():
            noraPathSelectDialog.setObjectName(u"noraPathSelectDialog")
        noraPathSelectDialog.resize(400, 300)
        self.horizontalLayoutWidget = QWidget(noraPathSelectDialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(40, 70, 331, 73))
        self.noraPathSelectHorizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.noraPathSelectHorizontalLayout.setObjectName(u"noraPathSelectHorizontalLayout")
        self.noraPathSelectHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.noraPathSelectHorizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.noraPathSelectHorizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.noraPathSelectHorizontalLayout.addWidget(self.pushButton)


        self.retranslateUi(noraPathSelectDialog)

        QMetaObject.connectSlotsByName(noraPathSelectDialog)
    # setupUi

    def retranslateUi(self, noraPathSelectDialog):
        noraPathSelectDialog.setWindowTitle(QCoreApplication.translate("noraPathSelectDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("noraPathSelectDialog", u"\u8def\u5f84\uff1a", None))
        self.pushButton.setText("")
    # retranslateUi

