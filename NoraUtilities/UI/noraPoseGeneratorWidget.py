# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraPoseGeneratorWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_noraPoseGeneratorWidget(object):
    def setupUi(self, noraPoseGeneratorWidget):
        if not noraPoseGeneratorWidget.objectName():
            noraPoseGeneratorWidget.setObjectName(u"noraPoseGeneratorWidget")
        noraPoseGeneratorWidget.resize(400, 95)
        self.verticalLayout_2 = QVBoxLayout(noraPoseGeneratorWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(noraPoseGeneratorWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.openPoseGenerator = QPushButton(self.groupBox)
        self.openPoseGenerator.setObjectName(u"openPoseGenerator")

        self.verticalLayout.addWidget(self.openPoseGenerator)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 136, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(noraPoseGeneratorWidget)

        QMetaObject.connectSlotsByName(noraPoseGeneratorWidget)
    # setupUi

    def retranslateUi(self, noraPoseGeneratorWidget):
        noraPoseGeneratorWidget.setWindowTitle(QCoreApplication.translate("noraPoseGeneratorWidget", u"Dialog", None))
        self.groupBox.setTitle("")
        self.openPoseGenerator.setText(QCoreApplication.translate("noraPoseGeneratorWidget", u"\u6253\u5f00\u5e27\u751f\u6210\u5668", None))
    # retranslateUi

