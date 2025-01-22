# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraListWidget.ui'
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
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_noraListDialog(object):
    def setupUi(self, noraListDialog):
        if not noraListDialog.objectName():
            noraListDialog.setObjectName(u"noraListDialog")
        noraListDialog.resize(792, 334)
        self.verticalLayoutWidget = QWidget(noraListDialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 391, 251))
        self.noraChannelListLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.noraChannelListLayout.setObjectName(u"noraChannelListLayout")
        self.noraChannelListLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.noraChannelListLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget = QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout.addWidget(self.listWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addButton = QPushButton(self.verticalLayoutWidget)
        self.addButton.setObjectName(u"addButton")

        self.verticalLayout.addWidget(self.addButton)

        self.removeButton = QPushButton(self.verticalLayoutWidget)
        self.removeButton.setObjectName(u"removeButton")

        self.verticalLayout.addWidget(self.removeButton)

        self.selectButton = QPushButton(self.verticalLayoutWidget)
        self.selectButton.setObjectName(u"selectButton")

        self.verticalLayout.addWidget(self.selectButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.noraChannelListLayout.addLayout(self.horizontalLayout)

        self.externVerticalLayout = QVBoxLayout()
        self.externVerticalLayout.setObjectName(u"externVerticalLayout")

        self.noraChannelListLayout.addLayout(self.externVerticalLayout)


        self.retranslateUi(noraListDialog)

        QMetaObject.connectSlotsByName(noraListDialog)
    # setupUi

    def retranslateUi(self, noraListDialog):
        noraListDialog.setWindowTitle(QCoreApplication.translate("noraListDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("noraListDialog", u"Label", None))
        self.addButton.setText(QCoreApplication.translate("noraListDialog", u"\u6dfb\u52a0", None))
        self.removeButton.setText(QCoreApplication.translate("noraListDialog", u"\u79fb\u9664", None))
        self.selectButton.setText(QCoreApplication.translate("noraListDialog", u"\u9009\u62e9", None))
    # retranslateUi

