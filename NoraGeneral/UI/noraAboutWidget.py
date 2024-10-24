# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraAboutWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QDialog, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_noraAboutWidget(object):
    def setupUi(self, noraAboutWidget):
        if not noraAboutWidget.objectName():
            noraAboutWidget.setObjectName(u"noraAboutWidget")
        noraAboutWidget.resize(460, 289)
        noraAboutWidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(noraAboutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(noraAboutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.linkButton = QCommandLinkButton(noraAboutWidget)
        self.linkButton.setObjectName(u"linkButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linkButton.sizePolicy().hasHeightForWidth())
        self.linkButton.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.linkButton)

        self.verticalSpacer = QSpacerItem(20, 201, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(noraAboutWidget)

        QMetaObject.connectSlotsByName(noraAboutWidget)
    # setupUi

    def retranslateUi(self, noraAboutWidget):
        noraAboutWidget.setWindowTitle(QCoreApplication.translate("noraAboutWidget", u"Dialog", None))
        self.label.setText("")
        self.linkButton.setText(QCoreApplication.translate("noraAboutWidget", u"Fast and Deep Deformation Approximations", None))
    # retranslateUi

