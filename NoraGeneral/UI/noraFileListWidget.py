# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraFileListWidget.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_noraFilePathListDialog(object):
    def setupUi(self, noraFilePathListDialog):
        if not noraFilePathListDialog.objectName():
            noraFilePathListDialog.setObjectName(u"noraFilePathListDialog")
        noraFilePathListDialog.resize(400, 300)
        self.verticalLayoutWidget = QWidget(noraFilePathListDialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 50, 321, 191))
        self.fileListVerticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.fileListVerticalLayout.setObjectName(u"fileListVerticalLayout")
        self.fileListVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.fileListVerticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listVerticalLayout = QVBoxLayout()
        self.listVerticalLayout.setObjectName(u"listVerticalLayout")

        self.horizontalLayout.addLayout(self.listVerticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.addPushButton = QPushButton(self.verticalLayoutWidget)
        self.addPushButton.setObjectName(u"addPushButton")

        self.verticalLayout_2.addWidget(self.addPushButton)

        self.removePushButton = QPushButton(self.verticalLayoutWidget)
        self.removePushButton.setObjectName(u"removePushButton")

        self.verticalLayout_2.addWidget(self.removePushButton)

        self.clearPushButton = QPushButton(self.verticalLayoutWidget)
        self.clearPushButton.setObjectName(u"clearPushButton")

        self.verticalLayout_2.addWidget(self.clearPushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.fileListVerticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(noraFilePathListDialog)

        QMetaObject.connectSlotsByName(noraFilePathListDialog)
    # setupUi

    def retranslateUi(self, noraFilePathListDialog):
        noraFilePathListDialog.setWindowTitle(QCoreApplication.translate("noraFilePathListDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("noraFilePathListDialog", u"\u6587\u4ef6\u5217\u8868\uff1a", None))
        self.addPushButton.setText("")
        self.removePushButton.setText("")
        self.clearPushButton.setText("")
    # retranslateUi

