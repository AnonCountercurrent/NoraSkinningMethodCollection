# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraStringInputWidget.ui'
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
    QLineEdit, QSizePolicy, QWidget)

class Ui_noraStringInputLayoutDialog(object):
    def setupUi(self, noraStringInputLayoutDialog):
        if not noraStringInputLayoutDialog.objectName():
            noraStringInputLayoutDialog.setObjectName(u"noraStringInputLayoutDialog")
        noraStringInputLayoutDialog.resize(400, 300)
        self.horizontalLayoutWidget = QWidget(noraStringInputLayoutDialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(50, 80, 311, 31))
        self.StringInputLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.StringInputLayout.setObjectName(u"StringInputLayout")
        self.StringInputLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.StringInputLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.StringInputLayout.addWidget(self.lineEdit)


        self.retranslateUi(noraStringInputLayoutDialog)

        QMetaObject.connectSlotsByName(noraStringInputLayoutDialog)
    # setupUi

    def retranslateUi(self, noraStringInputLayoutDialog):
        noraStringInputLayoutDialog.setWindowTitle(QCoreApplication.translate("noraStringInputLayoutDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("noraStringInputLayoutDialog", u"Text: ", None))
    # retranslateUi

