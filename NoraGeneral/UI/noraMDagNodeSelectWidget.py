# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraMDagNodeSelectWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_noraMDagNodeSelectWidget(object):
    def setupUi(self, noraMDagNodeSelectWidget):
        if not noraMDagNodeSelectWidget.objectName():
            noraMDagNodeSelectWidget.setObjectName(u"noraMDagNodeSelectWidget")
        noraMDagNodeSelectWidget.resize(650, 308)
        noraMDagNodeSelectWidget.setStyleSheet(u"")
        self.layoutWidget = QWidget(noraMDagNodeSelectWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 361, 31))
        self.selectLayout = QHBoxLayout(self.layoutWidget)
        self.selectLayout.setObjectName(u"selectLayout")
        self.selectLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.selectLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.selectLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.selectLayout.addWidget(self.pushButton)


        self.retranslateUi(noraMDagNodeSelectWidget)

        QMetaObject.connectSlotsByName(noraMDagNodeSelectWidget)
    # setupUi

    def retranslateUi(self, noraMDagNodeSelectWidget):
        noraMDagNodeSelectWidget.setWindowTitle(QCoreApplication.translate("noraMDagNodeSelectWidget", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("noraMDagNodeSelectWidget", u"label", None))
        self.pushButton.setText("")
    # retranslateUi

