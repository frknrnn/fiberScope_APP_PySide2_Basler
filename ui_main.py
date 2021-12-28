# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainfWzfkX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from zoom_preview import QtImageViewer_preview
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_tabBar = QFrame(self.frame_main)
        self.frame_tabBar.setObjectName(u"frame_tabBar")
        self.frame_tabBar.setMinimumSize(QSize(0, 50))
        self.frame_tabBar.setMaximumSize(QSize(16777215, 50))
        self.frame_tabBar.setFrameShape(QFrame.NoFrame)
        self.frame_tabBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_tabBar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_logo = QFrame(self.frame_tabBar)
        self.frame_logo.setObjectName(u"frame_logo")
        self.frame_logo.setMinimumSize(QSize(300, 0))
        self.frame_logo.setMaximumSize(QSize(300, 16777215))
        self.frame_logo.setFrameShape(QFrame.NoFrame)
        self.frame_logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_logo)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_logo_2 = QFrame(self.frame_logo)
        self.frame_logo_2.setObjectName(u"frame_logo_2")
        self.frame_logo_2.setMinimumSize(QSize(0, 50))
        self.frame_logo_2.setMaximumSize(QSize(300, 50))
        self.frame_logo_2.setToolTipDuration(0)
        self.frame_logo_2.setStyleSheet(u"background-image: url(:/icons/icons/logo.png);\n"
"border:none;\n"
"background-repeat: no-repeat;")
        self.frame_logo_2.setFrameShape(QFrame.NoFrame)
        self.frame_logo_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_logo_2)


        self.horizontalLayout_2.addWidget(self.frame_logo)

        self.frame_2 = QFrame(self.frame_tabBar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_window = QFrame(self.frame_tabBar)
        self.frame_window.setObjectName(u"frame_window")
        self.frame_window.setMinimumSize(QSize(150, 0))
        self.frame_window.setMaximumSize(QSize(150, 16777215))
        self.frame_window.setFrameShape(QFrame.NoFrame)
        self.frame_window.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_window)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_window_2 = QFrame(self.frame_window)
        self.frame_window_2.setObjectName(u"frame_window_2")
        self.frame_window_2.setMaximumSize(QSize(110, 16777215))
        self.frame_window_2.setFrameShape(QFrame.NoFrame)
        self.frame_window_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_window_2)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_minimize = QPushButton(self.frame_window_2)
        self.pushButton_minimize.setObjectName(u"pushButton_minimize")
        self.pushButton_minimize.setMinimumSize(QSize(30, 30))
        self.pushButton_minimize.setMaximumSize(QSize(30, 30))
        self.pushButton_minimize.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_minimize.setAutoFillBackground(False)
        self.pushButton_minimize.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/icons/icon_minimize.png);\n"
"	background-color: rgb(60, 60, 60);\n"
"border:none;\n"
"border-radius:15px;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(200, 200, 200);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}")
        self.pushButton_minimize.setAutoRepeat(False)
        self.pushButton_minimize.setAutoExclusive(False)
        self.pushButton_minimize.setAutoDefault(False)
        self.pushButton_minimize.setFlat(False)

        self.horizontalLayout_6.addWidget(self.pushButton_minimize)

        self.pushButton_maximize = QPushButton(self.frame_window_2)
        self.pushButton_maximize.setObjectName(u"pushButton_maximize")
        self.pushButton_maximize.setMinimumSize(QSize(30, 30))
        self.pushButton_maximize.setMaximumSize(QSize(30, 30))
        self.pushButton_maximize.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_maximize.setAutoFillBackground(False)
        self.pushButton_maximize.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/icons/icon_maximize.png);\n"
"background-color: rgb(60, 60, 60);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(200, 200, 200);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}")
        self.pushButton_maximize.setAutoRepeat(False)
        self.pushButton_maximize.setAutoExclusive(False)
        self.pushButton_maximize.setAutoDefault(False)
        self.pushButton_maximize.setFlat(False)

        self.horizontalLayout_6.addWidget(self.pushButton_maximize)

        self.pushButton_exit = QPushButton(self.frame_window_2)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setMinimumSize(QSize(30, 30))
        self.pushButton_exit.setMaximumSize(QSize(30, 30))
        self.pushButton_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_exit.setAutoFillBackground(False)
        self.pushButton_exit.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/icons/cil-x.png);\n"
"background-color: rgb(60, 60, 60);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius:15px;\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}")
        self.pushButton_exit.setAutoRepeat(False)
        self.pushButton_exit.setAutoExclusive(False)
        self.pushButton_exit.setAutoDefault(False)
        self.pushButton_exit.setFlat(False)

        self.horizontalLayout_6.addWidget(self.pushButton_exit)


        self.horizontalLayout_3.addWidget(self.frame_window_2)


        self.horizontalLayout_2.addWidget(self.frame_window)


        self.verticalLayout.addWidget(self.frame_tabBar)

        self.line = QFrame(self.frame_main)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.frame_scaffold = QFrame(self.frame_main)
        self.frame_scaffold.setObjectName(u"frame_scaffold")
        self.frame_scaffold.setFrameShape(QFrame.NoFrame)
        self.frame_scaffold.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_scaffold)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_scaffold)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_camera = QFrame(self.frame)
        self.frame_camera.setObjectName(u"frame_camera")
        self.frame_camera.setFrameShape(QFrame.NoFrame)
        self.frame_camera.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_camera)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.stackedWidget_2 = QStackedWidget(self.frame_camera)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pictureBox_preview = QtImageViewer_preview()
        self.pictureBox_preview.setObjectName(u"pictureBox_preview")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.pictureBox_preview.sizePolicy().hasHeightForWidth())
        self.pictureBox_preview.setSizePolicy(sizePolicy)
        self.pictureBox_preview.setMinimumSize(QSize(535, 0))
        self.pictureBox_preview.setMaximumSize(QSize(16777215, 16777215))
        self.pictureBox_preview.setMouseTracking(False)
        self.pictureBox_preview.setStyleSheet(u"QGraphicsView{\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"border:none;\n"
"}\n"
"\n"
" QScrollBar:horizontal\n"
"\n"
" {\n"
"\n"
"     height: 15px;\n"
"\n"
"     margin: 3px 15px 3px 15px;\n"
"\n"
"     border: 1px transparent #2A2929;\n"
"\n"
"     border-radius: 4px;\n"
"\n"
"     background-color:rgb(49, 51, 50) ;  \n"
"\n"
"	\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::handle:horizontal\n"
"\n"
" {\n"
"\n"
"     background-color: white;      /* #605F5F; */\n"
"\n"
"     min-width: 5px;\n"
"\n"
"     border-radius: 4px;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::add-line:horizontal\n"
"\n"
" {\n"
"\n"
"     margin: 0px 3px 0px 3px;\n"
"\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"\n"
"     width: 10px;\n"
"\n"
"     height: 10px;\n"
"\n"
"     subcontrol-position: right;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
"\n"
" {\n"
"\n"
"     margin: 0px 3px 0px 3px;\n"
"\n"
"     border-imag"
                        "e: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: left;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"\n"
" {\n"
"\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: right;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"\n"
" {\n"
"\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: left;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"\n"
" {\n"
"\n"
"     background: none;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QScrol"
                        "lBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"\n"
" {\n"
"\n"
"     background: none;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar:vertical\n"
"\n"
" {\n"
"\n"
"     \n"
"\n"
"	background-color: rgb(49, 51, 50);\n"
"\n"
"     width: 15px;\n"
"\n"
"     margin: 15px 3px 15px 3px;\n"
"\n"
"     border: 1px transparent #2A2929;\n"
"\n"
"     border-radius: 4px;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::handle:vertical\n"
"\n"
" {\n"
"\n"
"     background-color: white;         /* #605F5F; */\n"
"\n"
"     min-height: 5px;\n"
"\n"
"     border-radius: 4px;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::sub-line:vertical\n"
"\n"
" {\n"
"\n"
"     margin: 3px 0px 3px 0px;\n"
"\n"
"     border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: top;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::add-line:vertical\n"
"\n"
" {\n"
"\n"
"     margin: 3px 0px 3px 0px;\n"
"\n"
"     bor"
                        "der-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: bottom;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"\n"
" {\n"
"\n"
"\n"
"\n"
"     border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: top;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"\n"
" {\n"
"\n"
"     border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: bottom;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"\n"
" {\n"
"\n"
"     background: none;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" Q"
                        "ScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"\n"
" {\n"
"\n"
"     background: none;\n"
"\n"
" }")
        self.pictureBox_preview.setFrameShape(QFrame.NoFrame)
        self.pictureBox_preview.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.pictureBox_preview)

        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget_2.addWidget(self.page_4)

        self.verticalLayout_7.addWidget(self.stackedWidget_2)


        self.verticalLayout_3.addWidget(self.frame_camera)

        self.frame_bottomMenu = QFrame(self.frame)
        self.frame_bottomMenu.setObjectName(u"frame_bottomMenu")
        self.frame_bottomMenu.setMinimumSize(QSize(0, 60))
        self.frame_bottomMenu.setMaximumSize(QSize(16777215, 60))
        self.frame_bottomMenu.setFrameShape(QFrame.NoFrame)
        self.frame_bottomMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_bottomMenu)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_bottomMenu)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(600, 0))
        self.frame_5.setMaximumSize(QSize(600, 16777215))
        self.frame_5.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"\n"
"border-top-right-radius: 30px;")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_3 = QStackedWidget(self.frame_5)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"border-top-right-radius: 30px;")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_9 = QVBoxLayout(self.page_5)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.page_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"\n"
"border-top-right-radius: 30px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_lowerGrip_3 = QLabel(self.frame_7)
        self.label_lowerGrip_3.setObjectName(u"label_lowerGrip_3")
        self.label_lowerGrip_3.setGeometry(QRect(70, 20, 80, 20))
        self.label_lowerGrip_3.setStyleSheet(u"QLabel{\n"
"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"border:none;\n"
"}")
        self.checkBox_capture_8bit = QCheckBox(self.frame_7)
        self.checkBox_capture_8bit.setObjectName(u"checkBox_capture_8bit")
        self.checkBox_capture_8bit.setGeometry(QRect(160, 20, 80, 20))
        self.checkBox_capture_8bit.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"border:none;")
        self.checkBox_capture_16Bit = QCheckBox(self.frame_7)
        self.checkBox_capture_16Bit.setObjectName(u"checkBox_capture_16Bit")
        self.checkBox_capture_16Bit.setGeometry(QRect(240, 20, 80, 20))
        self.checkBox_capture_16Bit.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"border:none;")
        self.pushButton_cap = QPushButton(self.frame_7)
        self.pushButton_cap.setObjectName(u"pushButton_cap")
        self.pushButton_cap.setGeometry(QRect(340, 15, 120, 30))
        self.pushButton_cap.setMinimumSize(QSize(120, 30))
        self.pushButton_cap.setMaximumSize(QSize(120, 30))
        self.pushButton_cap.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_cap.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/icons/icons/capture.png);\n"
"background-color: rgba(150, 150, 150,100);\n"
"border-radius:15px;\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(0, 130, 0);\n"
"border-radius:15px;\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}")

        self.verticalLayout_9.addWidget(self.frame_7)

        self.stackedWidget_3.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.stackedWidget_3.addWidget(self.page_6)

        self.horizontalLayout_8.addWidget(self.stackedWidget_3)


        self.horizontalLayout_7.addWidget(self.frame_5)

        self.horizontalSpacer_2 = QSpacerItem(345, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_bottomMenu)


        self.horizontalLayout_4.addWidget(self.frame)

        self.frame_rightMenu = QFrame(self.frame_scaffold)
        self.frame_rightMenu.setObjectName(u"frame_rightMenu")
        self.frame_rightMenu.setMinimumSize(QSize(250, 0))
        self.frame_rightMenu.setMaximumSize(QSize(250, 16777215))
        self.frame_rightMenu.setStyleSheet(u"")
        self.frame_rightMenu.setFrameShape(QFrame.NoFrame)
        self.frame_rightMenu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_rightMenu)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_rightMenu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(30, 0))
        self.frame_4.setMaximumSize(QSize(30, 16777215))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_minimize_2 = QPushButton(self.frame_4)
        self.pushButton_minimize_2.setObjectName(u"pushButton_minimize_2")
        self.pushButton_minimize_2.setMinimumSize(QSize(25, 150))
        self.pushButton_minimize_2.setMaximumSize(QSize(25, 150))
        self.pushButton_minimize_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_minimize_2.setAutoFillBackground(False)
        self.pushButton_minimize_2.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/icons/preview_n.png);\n"
"background-color: rgb(200, 200, 200);\n"
"border:none;\n"
"border-radius:12px;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"qproperty-alignment: AlignVCenter;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(100, 100, 100);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}")
        self.pushButton_minimize_2.setAutoRepeat(False)
        self.pushButton_minimize_2.setAutoExclusive(False)
        self.pushButton_minimize_2.setAutoDefault(False)
        self.pushButton_minimize_2.setFlat(False)

        self.verticalLayout_4.addWidget(self.pushButton_minimize_2)

        self.pushButton_minimize_3 = QPushButton(self.frame_4)
        self.pushButton_minimize_3.setObjectName(u"pushButton_minimize_3")
        self.pushButton_minimize_3.setMinimumSize(QSize(25, 150))
        self.pushButton_minimize_3.setMaximumSize(QSize(25, 150))
        self.pushButton_minimize_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_minimize_3.setAutoFillBackground(False)
        self.pushButton_minimize_3.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/icons/video.png);\n"
"background-color: rgb(100, 100, 100);\n"
"border:none;\n"
"border-radius:12px;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"qproperty-alignment: AlignVCenter;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(200, 200, 200);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}")
        self.pushButton_minimize_3.setAutoRepeat(False)
        self.pushButton_minimize_3.setAutoExclusive(False)
        self.pushButton_minimize_3.setAutoDefault(False)
        self.pushButton_minimize_3.setFlat(False)

        self.verticalLayout_4.addWidget(self.pushButton_minimize_3)

        self.pushButton_minimize_4 = QPushButton(self.frame_4)
        self.pushButton_minimize_4.setObjectName(u"pushButton_minimize_4")
        self.pushButton_minimize_4.setMinimumSize(QSize(25, 150))
        self.pushButton_minimize_4.setMaximumSize(QSize(25, 150))
        self.pushButton_minimize_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_minimize_4.setAutoFillBackground(False)
        self.pushButton_minimize_4.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/icons/results.png);\n"
"background-color: rgb(100, 100, 100);\n"
"border:none;\n"
"border-radius:12px;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"qproperty-alignment: AlignVCenter;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color: rgb(200, 200, 200);\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}")
        self.pushButton_minimize_4.setAutoRepeat(False)
        self.pushButton_minimize_4.setAutoExclusive(False)
        self.pushButton_minimize_4.setAutoDefault(False)
        self.pushButton_minimize_4.setFlat(False)

        self.verticalLayout_4.addWidget(self.pushButton_minimize_4)

        self.verticalSpacer = QSpacerItem(20, 270, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame_rightMenu)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(230, 700))
        self.frame_3.setMaximumSize(QSize(230, 700))
        self.frame_3.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"border-bottom-left-radius: 115px;")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_6 = QVBoxLayout(self.page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"border-bottom-left-radius: 115px;")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 240, 181, 31))
        self.label.setStyleSheet(u"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 0, 181, 31))
        self.label_2.setStyleSheet(u"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.line_2 = QFrame(self.frame_6)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 30, 200, 3))
        self.line_2.setStyleSheet(u"background-color: rgb(100, 100, 100);")
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.frame_6)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(10, 270, 200, 3))
        self.line_3.setStyleSheet(u"background-color: rgb(100, 100, 100);")
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.frame_blue = QFrame(self.frame_6)
        self.frame_blue.setObjectName(u"frame_blue")
        self.frame_blue.setGeometry(QRect(50, 70, 110, 110))
        self.frame_blue.setMinimumSize(QSize(110, 110))
        self.frame_blue.setMaximumSize(QSize(110, 110))
        self.frame_blue.setFrameShape(QFrame.NoFrame)
        self.frame_blue.setFrameShadow(QFrame.Raised)
        self.frame_31 = QFrame(self.frame_blue)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setGeometry(QRect(30, 30, 50, 50))
        self.frame_31.setMinimumSize(QSize(50, 50))
        self.frame_31.setMaximumSize(QSize(50, 50))
        self.frame_31.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"border-radius :25px;")
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 40, 181, 20))
        self.label_3.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 300, 81, 20))
        self.label_4.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";")
        self.label_4.setFrameShape(QFrame.NoFrame)
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 340, 81, 20))
        self.label_5.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";")
        self.label_5.setFrameShape(QFrame.NoFrame)
        self.frame_blueSlider = QFrame(self.frame_6)
        self.frame_blueSlider.setObjectName(u"frame_blueSlider")
        self.frame_blueSlider.setGeometry(QRect(10, 190, 200, 30))
        self.frame_blueSlider.setMinimumSize(QSize(200, 30))
        self.frame_blueSlider.setMaximumSize(QSize(100, 30))
        self.frame_blueSlider.setFrameShape(QFrame.NoFrame)
        self.frame_blueSlider.setFrameShadow(QFrame.Raised)
        self.lineEdit_quickGain = QLineEdit(self.frame_6)
        self.lineEdit_quickGain.setObjectName(u"lineEdit_quickGain")
        self.lineEdit_quickGain.setGeometry(QRect(100, 340, 60, 20))
        self.lineEdit_quickGain.setMinimumSize(QSize(60, 20))
        self.lineEdit_quickGain.setMaximumSize(QSize(60, 20))
        self.lineEdit_quickGain.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_quickGain.setStyleSheet(u"QLineEdit{\n"
"font: 63 11pt \"Segoe UI Semibold\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(49, 51, 50);\n"
"border-radius:5px;\n"
"border-color:rgb(255, 255, 255);\n"
"border-width : 1px;\n"
"border-style:inset;\n"
"selection-background-color: rgb(0, 0, 0)\n"
"}\n"
"\n"
"\n"
"")
        self.lineEdit_quickGain.setAlignment(Qt.AlignCenter)
        self.pushButton_quickGain = QPushButton(self.frame_6)
        self.pushButton_quickGain.setObjectName(u"pushButton_quickGain")
        self.pushButton_quickGain.setGeometry(QRect(170, 340, 40, 20))
        self.pushButton_quickGain.setMinimumSize(QSize(40, 20))
        self.pushButton_quickGain.setMaximumSize(QSize(40, 20))
        self.pushButton_quickGain.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_quickGain.setStyleSheet(u"QPushButton{\n"
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
        self.lineEdit_quickExposure = QLineEdit(self.frame_6)
        self.lineEdit_quickExposure.setObjectName(u"lineEdit_quickExposure")
        self.lineEdit_quickExposure.setGeometry(QRect(100, 300, 60, 20))
        self.lineEdit_quickExposure.setMinimumSize(QSize(60, 20))
        self.lineEdit_quickExposure.setMaximumSize(QSize(60, 20))
        self.lineEdit_quickExposure.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_quickExposure.setStyleSheet(u"QLineEdit{\n"
"font: 63 11pt \"Segoe UI Semibold\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(49, 51, 50);\n"
"border-radius:5px;\n"
"border-color:rgb(255, 255, 255);\n"
"border-width : 1px;\n"
"border-style:inset;\n"
"selection-background-color: rgb(0, 0, 0)\n"
"}\n"
"\n"
"\n"
"")
        self.lineEdit_quickExposure.setAlignment(Qt.AlignCenter)
        self.pushButton_quickExposure = QPushButton(self.frame_6)
        self.pushButton_quickExposure.setObjectName(u"pushButton_quickExposure")
        self.pushButton_quickExposure.setGeometry(QRect(170, 300, 40, 20))
        self.pushButton_quickExposure.setMinimumSize(QSize(40, 20))
        self.pushButton_quickExposure.setMaximumSize(QSize(40, 20))
        self.pushButton_quickExposure.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_quickExposure.setStyleSheet(u"QPushButton{\n"
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
        self.radioButton_8bit = QRadioButton(self.frame_6)
        self.radioButton_8bit.setObjectName(u"radioButton_8bit")
        self.radioButton_8bit.setGeometry(QRect(90, 385, 63, 15))
        self.radioButton_8bit.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";")
        self.radioButton_16bit = QRadioButton(self.frame_6)
        self.radioButton_16bit.setObjectName(u"radioButton_16bit")
        self.radioButton_16bit.setGeometry(QRect(150, 385, 61, 16))
        self.radioButton_16bit.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";")
        self.label_lowerGrip_2 = QLabel(self.frame_6)
        self.label_lowerGrip_2.setObjectName(u"label_lowerGrip_2")
        self.label_lowerGrip_2.setGeometry(QRect(10, 380, 71, 20))
        self.label_lowerGrip_2.setStyleSheet(u"QLabel{\n"
"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"border:none;\n"
"}")
        self.checkBox = QCheckBox(self.frame_6)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 480, 91, 13))
        self.checkBox.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"font: 87 8pt \"Segoe UI Black\";")
        self.label_upperGrip = QLabel(self.frame_6)
        self.label_upperGrip.setObjectName(u"label_upperGrip")
        self.label_upperGrip.setGeometry(QRect(110, 510, 101, 22))
        self.label_upperGrip.setStyleSheet(u"QLabel{\n"
"color: rgb(200, 200, 200);\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"border:none;\n"
"}")
        self.label_lowerGrip = QLabel(self.frame_6)
        self.label_lowerGrip.setObjectName(u"label_lowerGrip")
        self.label_lowerGrip.setGeometry(QRect(10, 510, 101, 22))
        self.label_lowerGrip.setStyleSheet(u"QLabel{\n"
"color: rgb(200, 200, 200);\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"border:none;\n"
"}")
        self.line_4 = QFrame(self.frame_6)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(10, 460, 200, 3))
        self.line_4.setStyleSheet(u"background-color: rgb(100, 100, 100);")
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 430, 181, 21))
        self.label_6.setStyleSheet(u"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.frame_lut = QFrame(self.frame_6)
        self.frame_lut.setObjectName(u"frame_lut")
        self.frame_lut.setGeometry(QRect(50, 550, 110, 110))
        self.frame_lut.setMinimumSize(QSize(110, 110))
        self.frame_lut.setMaximumSize(QSize(110, 110))
        self.frame_lut.setFrameShape(QFrame.NoFrame)
        self.frame_lut.setFrameShadow(QFrame.Raised)
        self.frame_32 = QFrame(self.frame_lut)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setGeometry(QRect(30, 30, 50, 50))
        self.frame_32.setMinimumSize(QSize(50, 50))
        self.frame_32.setMaximumSize(QSize(50, 50))
        self.frame_32.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"border-radius :25px;")
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_5.addWidget(self.frame_3, 0, Qt.AlignTop)


        self.horizontalLayout_4.addWidget(self.frame_rightMenu)


        self.verticalLayout.addWidget(self.frame_scaffold)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_minimize.setDefault(False)
        self.pushButton_maximize.setDefault(False)
        self.pushButton_exit.setDefault(False)
        self.stackedWidget_3.setCurrentIndex(0)
        self.pushButton_minimize_2.setDefault(False)
        self.pushButton_minimize_3.setDefault(False)
        self.pushButton_minimize_4.setDefault(False)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.pushButton_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_exit.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_exit.setText("")
        self.label_lowerGrip_3.setText(QCoreApplication.translate("MainWindow", u"Bit Depth : ", None))
        self.checkBox_capture_8bit.setText(QCoreApplication.translate("MainWindow", u"8 Bit", None))
        self.checkBox_capture_16Bit.setText(QCoreApplication.translate("MainWindow", u"16 Bit", None))
        self.pushButton_cap.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_minimize_2.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_minimize_2.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_minimize_3.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_minimize_3.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_minimize_4.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_minimize_4.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Camera Settings", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Led Settings ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Blue Channel : ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Exposure (s) : ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Gain (0-23) : ", None))
        self.lineEdit_quickGain.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_quickGain.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.lineEdit_quickExposure.setText(QCoreApplication.translate("MainWindow", u"0.001", None))
        self.pushButton_quickExposure.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.radioButton_8bit.setText(QCoreApplication.translate("MainWindow", u"8 Bit", None))
        self.radioButton_16bit.setText(QCoreApplication.translate("MainWindow", u"16 Bit", None))
        self.label_lowerGrip_2.setText(QCoreApplication.translate("MainWindow", u"Bit Depth : ", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Auto LUT", None))
        self.label_upperGrip.setText(QCoreApplication.translate("MainWindow", u"Upper Grip: 39000", None))
        self.label_lowerGrip.setText(QCoreApplication.translate("MainWindow", u"Lower Grip : 100", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"LUT", None))
    # retranslateUi

