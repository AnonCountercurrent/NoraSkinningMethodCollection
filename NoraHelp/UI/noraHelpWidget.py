# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraHelpWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QDialog, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_noraHelpWidget(object):
    def setupUi(self, noraHelpWidget):
        if not noraHelpWidget.objectName():
            noraHelpWidget.setObjectName(u"noraHelpWidget")
        noraHelpWidget.resize(466, 500)
        self.verticalLayout_2 = QVBoxLayout(noraHelpWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(noraHelpWidget)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(0, 200))
        self.IconLabel = QLabel(self.widget)
        self.IconLabel.setObjectName(u"IconLabel")
        self.IconLabel.setGeometry(QRect(10, 30, 128, 128))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 40, 251, 71))
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setText(u"Nora SMC")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 100, 611, 31))
        font1 = QFont()
        font1.setFamilies([u"\u5e7c\u5706"])
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setText(u"Nora Skinning Method Collection")

        self.verticalLayout_2.addWidget(self.widget)

        self.label_6 = QLabel(noraHelpWidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(0, 30))
        self.label_6.setFont(font1)
        self.label_6.setText(u"\u76f8\u5173\u6587\u6863\u94fe\u63a5\uff1a")

        self.verticalLayout_2.addWidget(self.label_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(noraHelpWidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setMinimumSize(QSize(30, 0))

        self.horizontalLayout.addWidget(self.widget_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gotoDocs = QCommandLinkButton(noraHelpWidget)
        self.gotoDocs.setObjectName(u"gotoDocs")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.gotoDocs.sizePolicy().hasHeightForWidth())
        self.gotoDocs.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(9)
        font2.setUnderline(True)
        self.gotoDocs.setFont(font2)
        self.gotoDocs.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.gotoDocs.setText(u"Docs URL")
        self.gotoDocs.setAutoDefault(True)

        self.verticalLayout.addWidget(self.gotoDocs)

        self.gotoCreatedBy = QCommandLinkButton(noraHelpWidget)
        self.gotoCreatedBy.setObjectName(u"gotoCreatedBy")
        self.gotoCreatedBy.setFont(font2)
        self.gotoCreatedBy.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
#if QT_CONFIG(accessibility)
        self.gotoCreatedBy.setAccessibleDescription(u"")
#endif // QT_CONFIG(accessibility)
        self.gotoCreatedBy.setText(u"Created By URL")

        self.verticalLayout.addWidget(self.gotoCreatedBy)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 153, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(noraHelpWidget)

        QMetaObject.connectSlotsByName(noraHelpWidget)
    # setupUi

    def retranslateUi(self, noraHelpWidget):
        noraHelpWidget.setWindowTitle(QCoreApplication.translate("noraHelpWidget", u"Dialog", None))
        self.IconLabel.setText("")
    # retranslateUi

