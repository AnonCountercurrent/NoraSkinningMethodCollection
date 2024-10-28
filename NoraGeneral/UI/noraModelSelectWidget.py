# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraModelSelectWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_noraModelSelectedWidget(object):
    def setupUi(self, noraModelSelectedWidget):
        if not noraModelSelectedWidget.objectName():
            noraModelSelectedWidget.setObjectName(u"noraModelSelectedWidget")
        noraModelSelectedWidget.resize(650, 308)
        noraModelSelectedWidget.setStyleSheet(u"")
        self.verticalLayoutWidget = QWidget(noraModelSelectedWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 541, 111))
        self.modelSelectWithFrameRangeLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.modelSelectWithFrameRangeLayout.setObjectName(u"modelSelectWithFrameRangeLayout")
        self.modelSelectWithFrameRangeLayout.setContentsMargins(0, 0, 0, 0)
        self.modelSelectLayout = QVBoxLayout()
        self.modelSelectLayout.setObjectName(u"modelSelectLayout")

        self.modelSelectWithFrameRangeLayout.addLayout(self.modelSelectLayout)

        self.frameRangeLayout = QHBoxLayout()
        self.frameRangeLayout.setObjectName(u"frameRangeLayout")

        self.modelSelectWithFrameRangeLayout.addLayout(self.frameRangeLayout)


        self.retranslateUi(noraModelSelectedWidget)

        QMetaObject.connectSlotsByName(noraModelSelectedWidget)
    # setupUi

    def retranslateUi(self, noraModelSelectedWidget):
        noraModelSelectedWidget.setWindowTitle(QCoreApplication.translate("noraModelSelectedWidget", u"Dialog", None))
    # retranslateUi

