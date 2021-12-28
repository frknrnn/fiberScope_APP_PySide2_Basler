# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splashLQxlxh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 300)
        MainWindow.setMaximumSize(QSize(500, 300))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(500, 300))
        self.frame.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"border-radius: 20px;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_tab = QFrame(self.frame)
        self.frame_tab.setObjectName(u"frame_tab")
        self.frame_tab.setMinimumSize(QSize(0, 100))
        self.frame_tab.setMaximumSize(QSize(16777215, 100))
        self.frame_tab.setFrameShape(QFrame.NoFrame)
        self.frame_tab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_logo_2 = QFrame(self.frame_tab)
        self.frame_logo_2.setObjectName(u"frame_logo_2")
        self.frame_logo_2.setMinimumSize(QSize(370, 50))
        self.frame_logo_2.setMaximumSize(QSize(370, 50))
        self.frame_logo_2.setToolTipDuration(0)
        self.frame_logo_2.setStyleSheet(u"background-image: url(:/icons/icons/fiberScope_.png);\n"
"border:none;\n"
"background-repeat: no-repeat;")
        self.frame_logo_2.setFrameShape(QFrame.NoFrame)
        self.frame_logo_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_logo_2, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_tab)

        self.frame_bottom = QFrame(self.frame)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_bottom)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame_bottom)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.comboBox_comPort = QComboBox(self.frame_2)
        self.comboBox_comPort.setObjectName(u"comboBox_comPort")
        self.comboBox_comPort.setMinimumSize(QSize(0, 35))
        self.comboBox_comPort.setMaximumSize(QSize(16777215, 35))
        self.comboBox_comPort.setStyleSheet(u"QComboBox{\n"
"font: 63 12pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:2px;\n"
"border-none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"}\n"
"QComboBox QAbstractItemView{border: 0px;color:white}")

        self.gridLayout.addWidget(self.comboBox_comPort, 0, 1, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.comboBox_baudRate = QComboBox(self.frame_2)
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.addItem("")
        self.comboBox_baudRate.setObjectName(u"comboBox_baudRate")
        self.comboBox_baudRate.setMinimumSize(QSize(0, 35))
        self.comboBox_baudRate.setMaximumSize(QSize(16777215, 35))
        self.comboBox_baudRate.setStyleSheet(u"QComboBox{\n"
"font: 63 12pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:2px;\n"
"border-none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"}\n"
"QComboBox QAbstractItemView{border: 0px;color:white}")

        self.gridLayout.addWidget(self.comboBox_baudRate, 1, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame_bottom)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_quit = QPushButton(self.frame_3)
        self.pushButton_quit.setObjectName(u"pushButton_quit")
        self.pushButton_quit.setMinimumSize(QSize(120, 30))
        self.pushButton_quit.setMaximumSize(QSize(120, 30))
        self.pushButton_quit.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_quit.setStyleSheet(u"QPushButton{\n"
"font: 63 11pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(150, 150, 150,100);\n"
"border-radius:4px;\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(130, 0, 0);\n"
"border-radius:4px;\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_quit)

        self.pushButton_connect = QPushButton(self.frame_3)
        self.pushButton_connect.setObjectName(u"pushButton_connect")
        self.pushButton_connect.setMinimumSize(QSize(120, 30))
        self.pushButton_connect.setMaximumSize(QSize(120, 30))
        self.pushButton_connect.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_connect.setStyleSheet(u"QPushButton{\n"
"font: 63 11pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(150, 150, 150,100);\n"
"border-radius:4px;\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(0, 130, 0);\n"
"border-radius:4px;\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_connect)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame_bottom)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Com Port", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Baud Rate", None))
        self.comboBox_baudRate.setItemText(0, QCoreApplication.translate("MainWindow", u"9600", None))
        self.comboBox_baudRate.setItemText(1, QCoreApplication.translate("MainWindow", u"14400", None))
        self.comboBox_baudRate.setItemText(2, QCoreApplication.translate("MainWindow", u"19200", None))
        self.comboBox_baudRate.setItemText(3, QCoreApplication.translate("MainWindow", u"38400", None))
        self.comboBox_baudRate.setItemText(4, QCoreApplication.translate("MainWindow", u"57600", None))
        self.comboBox_baudRate.setItemText(5, QCoreApplication.translate("MainWindow", u"115200", None))

        self.pushButton_quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.pushButton_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
    # retranslateUi

