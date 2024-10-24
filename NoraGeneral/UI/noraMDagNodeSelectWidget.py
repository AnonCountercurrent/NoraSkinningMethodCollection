# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraMDagNodeSelectWidget.ui'
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(60, 0))

        self.selectLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.selectLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(40, 0))
        self.pushButton.setMaximumSize(QSize(40, 16777215))

        self.selectLayout.addWidget(self.pushButton)


        self.retranslateUi(noraMDagNodeSelectWidget)

        QMetaObject.connectSlotsByName(noraMDagNodeSelectWidget)
    # setupUi

    def retranslateUi(self, noraMDagNodeSelectWidget):
        noraMDagNodeSelectWidget.setWindowTitle(QCoreApplication.translate("noraMDagNodeSelectWidget", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("noraMDagNodeSelectWidget", u"label", None))
        self.pushButton.setText("")
    # retranslateUi

