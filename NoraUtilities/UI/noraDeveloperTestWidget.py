# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'noraDeveloperTestWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QGroupBox,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_noraDeveloperTestWidget(object):
    def setupUi(self, noraDeveloperTestWidget):
        if not noraDeveloperTestWidget.objectName():
            noraDeveloperTestWidget.setObjectName(u"noraDeveloperTestWidget")
        noraDeveloperTestWidget.resize(435, 355)
        self.verticalLayout_2 = QVBoxLayout(noraDeveloperTestWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(noraDeveloperTestWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.doubleSpinBox = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setDecimals(14)
        self.doubleSpinBox.setMinimum(-9999999999999.000000000000000)
        self.doubleSpinBox.setMaximum(9999999999999.000000000000000)
        self.doubleSpinBox.setSingleStep(1.000000000000000)
        self.doubleSpinBox.setValue(123.456789000000001)

        self.verticalLayout.addWidget(self.doubleSpinBox)

        self.testPushButton = QPushButton(self.groupBox)
        self.testPushButton.setObjectName(u"testPushButton")

        self.verticalLayout.addWidget(self.testPushButton)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.verticalSpacer = QSpacerItem(20, 273, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(noraDeveloperTestWidget)

        QMetaObject.connectSlotsByName(noraDeveloperTestWidget)
    # setupUi

    def retranslateUi(self, noraDeveloperTestWidget):
        noraDeveloperTestWidget.setWindowTitle(QCoreApplication.translate("noraDeveloperTestWidget", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("noraDeveloperTestWidget", u"Test", None))
        self.testPushButton.setText(QCoreApplication.translate("noraDeveloperTestWidget", u"Test", None))
    # retranslateUi

