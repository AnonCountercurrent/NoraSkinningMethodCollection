# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraPoseGeneratorWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_noraPoseGeneratorWindow(object):
    def setupUi(self, noraPoseGeneratorWindow):
        if not noraPoseGeneratorWindow.objectName():
            noraPoseGeneratorWindow.setObjectName(u"noraPoseGeneratorWindow")
        noraPoseGeneratorWindow.resize(813, 625)
        noraPoseGeneratorWindow.setStyleSheet(u"font: 9pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.verticalLayout_3 = QVBoxLayout(noraPoseGeneratorWindow)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.saveButton = QPushButton(noraPoseGeneratorWindow)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout.addWidget(self.saveButton)

        self.readButton = QPushButton(noraPoseGeneratorWindow)
        self.readButton.setObjectName(u"readButton")

        self.horizontalLayout.addWidget(self.readButton)

        self.refreshButton = QPushButton(noraPoseGeneratorWindow)
        self.refreshButton.setObjectName(u"refreshButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshButton.sizePolicy().hasHeightForWidth())
        self.refreshButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.refreshButton)

        self.line_2 = QFrame(noraPoseGeneratorWindow)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.settingsButton = QPushButton(noraPoseGeneratorWindow)
        self.settingsButton.setObjectName(u"settingsButton")

        self.horizontalLayout.addWidget(self.settingsButton)

        self.addButton = QPushButton(noraPoseGeneratorWindow)
        self.addButton.setObjectName(u"addButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.addButton)

        self.line_3 = QFrame(noraPoseGeneratorWindow)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.horizontalSpacer = QSpacerItem(1, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.LastConfigPath = QLineEdit(noraPoseGeneratorWindow)
        self.LastConfigPath.setObjectName(u"LastConfigPath")
        self.LastConfigPath.setMinimumSize(QSize(300, 0))

        self.horizontalLayout.addWidget(self.LastConfigPath)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.line = QFrame(noraPoseGeneratorWindow)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.splitter = QSplitter(noraPoseGeneratorWindow)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.verticalLayoutWidget = QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 1)
        self.tableWidget = QTableWidget(self.groupBox_3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setColumnCount(0)

        self.horizontalLayout_2.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.splitter.addWidget(self.verticalLayoutWidget)
        self.verticalLayoutWidget_2 = QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ChannelSetings = QGroupBox(self.verticalLayoutWidget_2)
        self.ChannelSetings.setObjectName(u"ChannelSetings")
        self.verticalLayout_5 = QVBoxLayout(self.ChannelSetings)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.ChannelPropertiesLayout = QGridLayout()
        self.ChannelPropertiesLayout.setObjectName(u"ChannelPropertiesLayout")

        self.verticalLayout_5.addLayout(self.ChannelPropertiesLayout)


        self.verticalLayout_2.addWidget(self.ChannelSetings)

        self.GeneratorSettings = QGroupBox(self.verticalLayoutWidget_2)
        self.GeneratorSettings.setObjectName(u"GeneratorSettings")
        self.horizontalLayout_4 = QHBoxLayout(self.GeneratorSettings)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.GeneratorSettingsLayout = QGridLayout()
        self.GeneratorSettingsLayout.setObjectName(u"GeneratorSettingsLayout")

        self.horizontalLayout_4.addLayout(self.GeneratorSettingsLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addWidget(self.GeneratorSettings)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.ExecuteGroup = QGroupBox(self.verticalLayoutWidget_2)
        self.ExecuteGroup.setObjectName(u"ExecuteGroup")
        self.horizontalLayout_3 = QHBoxLayout(self.ExecuteGroup)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.GenerateButton = QPushButton(self.ExecuteGroup)
        self.GenerateButton.setObjectName(u"GenerateButton")

        self.horizontalLayout_3.addWidget(self.GenerateButton)


        self.verticalLayout_2.addWidget(self.ExecuteGroup)

        self.splitter.addWidget(self.verticalLayoutWidget_2)

        self.verticalLayout_3.addWidget(self.splitter)


        self.retranslateUi(noraPoseGeneratorWindow)

        QMetaObject.connectSlotsByName(noraPoseGeneratorWindow)
    # setupUi

    def retranslateUi(self, noraPoseGeneratorWindow):
        noraPoseGeneratorWindow.setWindowTitle(QCoreApplication.translate("noraPoseGeneratorWindow", u"Dialog", None))
#if QT_CONFIG(tooltip)
        noraPoseGeneratorWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.saveButton.setToolTip(QCoreApplication.translate("noraPoseGeneratorWindow", u"\u4fdd\u5b58\u914d\u7f6e", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.saveButton.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.saveButton.setText("")
#if QT_CONFIG(tooltip)
        self.readButton.setToolTip(QCoreApplication.translate("noraPoseGeneratorWindow", u"\u8bfb\u53d6\u914d\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.readButton.setText("")
#if QT_CONFIG(tooltip)
        self.refreshButton.setToolTip(QCoreApplication.translate("noraPoseGeneratorWindow", u"\u91cd\u65b0\u8bfb\u53d6\u5f53\u524d\u914d\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.refreshButton.setText("")
#if QT_CONFIG(tooltip)
        self.settingsButton.setToolTip(QCoreApplication.translate("noraPoseGeneratorWindow", u"\u8bbe\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.settingsButton.setText("")
#if QT_CONFIG(tooltip)
        self.addButton.setToolTip(QCoreApplication.translate("noraPoseGeneratorWindow", u"\u6dfb\u52a0\u9009\u4e2d\u5bf9\u8c61", None))
#endif // QT_CONFIG(tooltip)
        self.addButton.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("noraPoseGeneratorWindow", u"Channels:", None))
        self.ChannelSetings.setTitle(QCoreApplication.translate("noraPoseGeneratorWindow", u"Channel Properties", None))
        self.GeneratorSettings.setTitle(QCoreApplication.translate("noraPoseGeneratorWindow", u"Generator Settings", None))
        self.ExecuteGroup.setTitle("")
        self.GenerateButton.setText(QCoreApplication.translate("noraPoseGeneratorWindow", u"\u751f\u6210", None))
    # retranslateUi

