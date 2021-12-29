# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maingCHcae.ui'
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
        self.verticalLayout.setSpacing(0)
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
        self.line.setStyleSheet(u"background-color: rgb(100, 100, 100);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.stackedWidget_mainPage = QStackedWidget(self.frame_main)
        self.stackedWidget_mainPage.setObjectName(u"stackedWidget_mainPage")
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.verticalLayout_12 = QVBoxLayout(self.page_10)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_scaffold = QFrame(self.page_10)
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
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_camera = QStackedWidget(self.frame_camera)
        self.stackedWidget_camera.setObjectName(u"stackedWidget_camera")
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

        self.stackedWidget_camera.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_14 = QVBoxLayout(self.page_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.pictureBox_result = QtImageViewer_preview()
        self.pictureBox_result.setObjectName(u"pictureBox_result")
        sizePolicy.setHeightForWidth(self.pictureBox_result.sizePolicy().hasHeightForWidth())
        self.pictureBox_result.setSizePolicy(sizePolicy)
        self.pictureBox_result.setMinimumSize(QSize(535, 0))
        self.pictureBox_result.setMaximumSize(QSize(16777215, 16777215))
        self.pictureBox_result.setMouseTracking(False)
        self.pictureBox_result.setStyleSheet(u"QGraphicsView{\n"
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
        self.pictureBox_result.setFrameShape(QFrame.NoFrame)
        self.pictureBox_result.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.pictureBox_result)

        self.stackedWidget_camera.addWidget(self.page_4)

        self.verticalLayout_7.addWidget(self.stackedWidget_camera)


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
        self.stackedWidget_bottom = QStackedWidget(self.frame_5)
        self.stackedWidget_bottom.setObjectName(u"stackedWidget_bottom")
        self.stackedWidget_bottom.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
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
        self.label_lowerGrip_3.setGeometry(QRect(30, 20, 91, 18))
        self.label_lowerGrip_3.setStyleSheet(u"QLabel{\n"
"color: rgb(200, 200, 200);\n"
"font: 87 12pt \"Segoe UI Black\";\n"
"border:none;\n"
"}")
        self.pushButton_cap = QPushButton(self.frame_7)
        self.pushButton_cap.setObjectName(u"pushButton_cap")
        self.pushButton_cap.setGeometry(QRect(410, 15, 120, 30))
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
        self.frame_16bit = QFrame(self.frame_7)
        self.frame_16bit.setObjectName(u"frame_16bit")
        self.frame_16bit.setGeometry(QRect(190, 12, 60, 30))
        self.frame_16bit.setMinimumSize(QSize(60, 30))
        self.frame_16bit.setMaximumSize(QSize(60, 30))
        self.frame_16bit.setStyleSheet(u"\n"
"border-radius:none;")
        self.frame_16bit.setFrameShape(QFrame.NoFrame)
        self.frame_16bit.setFrameShadow(QFrame.Raised)
        self.frame_8bit = QFrame(self.frame_7)
        self.frame_8bit.setObjectName(u"frame_8bit")
        self.frame_8bit.setGeometry(QRect(320, 12, 60, 30))
        self.frame_8bit.setMinimumSize(QSize(60, 30))
        self.frame_8bit.setMaximumSize(QSize(60, 30))
        self.frame_8bit.setStyleSheet(u"\n"
"border-radius:none;")
        self.frame_8bit.setFrameShape(QFrame.NoFrame)
        self.frame_8bit.setFrameShadow(QFrame.Raised)
        self.label_lowerGrip_4 = QLabel(self.frame_7)
        self.label_lowerGrip_4.setObjectName(u"label_lowerGrip_4")
        self.label_lowerGrip_4.setGeometry(QRect(150, 20, 31, 20))
        self.label_lowerGrip_4.setStyleSheet(u"QLabel{\n"
"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"border:none;\n"
"}")
        self.label_lowerGrip_5 = QLabel(self.frame_7)
        self.label_lowerGrip_5.setObjectName(u"label_lowerGrip_5")
        self.label_lowerGrip_5.setGeometry(QRect(280, 20, 41, 20))
        self.label_lowerGrip_5.setStyleSheet(u"QLabel{\n"
"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"border:none;\n"
"}")

        self.verticalLayout_9.addWidget(self.frame_7)

        self.stackedWidget_bottom.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.horizontalLayout_9 = QHBoxLayout(self.page_6)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.page_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"\n"
"border-top-right-radius: 30px;")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_resultTimeSeriesEnabled = QFrame(self.frame_8)
        self.frame_resultTimeSeriesEnabled.setObjectName(u"frame_resultTimeSeriesEnabled")
        self.frame_resultTimeSeriesEnabled.setFrameShape(QFrame.NoFrame)
        self.frame_resultTimeSeriesEnabled.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_resultTimeSeriesEnabled)
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 5, 0, 5)
        self.frame_104 = QFrame(self.frame_resultTimeSeriesEnabled)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setMinimumSize(QSize(120, 0))
        self.frame_104.setMaximumSize(QSize(120, 16777215))
        self.frame_104.setFrameShape(QFrame.NoFrame)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_104)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame_104)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"font: 63 10pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.label_38.setFrameShadow(QFrame.Plain)
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_51.addWidget(self.label_38)


        self.horizontalLayout_16.addWidget(self.frame_104)

        self.pushButton_resultCaptureLeft = QPushButton(self.frame_resultTimeSeriesEnabled)
        self.pushButton_resultCaptureLeft.setObjectName(u"pushButton_resultCaptureLeft")
        self.pushButton_resultCaptureLeft.setMinimumSize(QSize(25, 25))
        self.pushButton_resultCaptureLeft.setMaximumSize(QSize(25, 25))
        self.pushButton_resultCaptureLeft.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_resultCaptureLeft.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/icons/icons/left_.png);\n"
"border-radius:4px;\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgba(200, 200, 200,100);\n"
"border-radius:4px;\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}")

        self.horizontalLayout_16.addWidget(self.pushButton_resultCaptureLeft)

        self.frame_resultCaptureSlider = QFrame(self.frame_resultTimeSeriesEnabled)
        self.frame_resultCaptureSlider.setObjectName(u"frame_resultCaptureSlider")
        self.frame_resultCaptureSlider.setMinimumSize(QSize(300, 0))
        self.frame_resultCaptureSlider.setMaximumSize(QSize(300, 16777215))
        self.frame_resultCaptureSlider.setFrameShape(QFrame.NoFrame)
        self.frame_resultCaptureSlider.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_16.addWidget(self.frame_resultCaptureSlider)

        self.pushButton_resultCaptureRight = QPushButton(self.frame_resultTimeSeriesEnabled)
        self.pushButton_resultCaptureRight.setObjectName(u"pushButton_resultCaptureRight")
        self.pushButton_resultCaptureRight.setMinimumSize(QSize(25, 25))
        self.pushButton_resultCaptureRight.setMaximumSize(QSize(25, 25))
        self.pushButton_resultCaptureRight.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_resultCaptureRight.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/icons/icons/right_.png);\n"
"border-radius:4px;\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgba(200, 200, 200,100);\n"
"border-radius:4px;\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}")

        self.horizontalLayout_16.addWidget(self.pushButton_resultCaptureRight)

        self.frame_111 = QFrame(self.frame_resultTimeSeriesEnabled)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setMinimumSize(QSize(100, 0))
        self.frame_111.setMaximumSize(QSize(100, 16777215))
        self.frame_111.setFrameShape(QFrame.NoFrame)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_111)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_resultCaptureIndex = QLabel(self.frame_111)
        self.label_resultCaptureIndex.setObjectName(u"label_resultCaptureIndex")
        self.label_resultCaptureIndex.setStyleSheet(u"font: 63 10pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border:none;")
        self.label_resultCaptureIndex.setFrameShadow(QFrame.Plain)
        self.label_resultCaptureIndex.setAlignment(Qt.AlignCenter)

        self.verticalLayout_53.addWidget(self.label_resultCaptureIndex)


        self.horizontalLayout_16.addWidget(self.frame_111)


        self.horizontalLayout_10.addWidget(self.frame_resultTimeSeriesEnabled)


        self.horizontalLayout_9.addWidget(self.frame_8)

        self.stackedWidget_bottom.addWidget(self.page_6)

        self.horizontalLayout_8.addWidget(self.stackedWidget_bottom)


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
        self.pushButton_preview = QPushButton(self.frame_4)
        self.pushButton_preview.setObjectName(u"pushButton_preview")
        self.pushButton_preview.setMinimumSize(QSize(25, 150))
        self.pushButton_preview.setMaximumSize(QSize(25, 150))
        self.pushButton_preview.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_preview.setAutoFillBackground(False)
        self.pushButton_preview.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/icons/preview_n.png);\n"
"background-color: rgb(200, 200, 200);\n"
"border:none;\n"
"border-radius:12px;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}")
        self.pushButton_preview.setAutoRepeat(False)
        self.pushButton_preview.setAutoExclusive(False)
        self.pushButton_preview.setAutoDefault(False)
        self.pushButton_preview.setFlat(False)

        self.verticalLayout_4.addWidget(self.pushButton_preview)

        self.pushButton_video = QPushButton(self.frame_4)
        self.pushButton_video.setObjectName(u"pushButton_video")
        self.pushButton_video.setMinimumSize(QSize(25, 150))
        self.pushButton_video.setMaximumSize(QSize(25, 150))
        self.pushButton_video.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_video.setAutoFillBackground(False)
        self.pushButton_video.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_video.setAutoRepeat(False)
        self.pushButton_video.setAutoExclusive(False)
        self.pushButton_video.setAutoDefault(False)
        self.pushButton_video.setFlat(False)

        self.verticalLayout_4.addWidget(self.pushButton_video)

        self.pushButton_results = QPushButton(self.frame_4)
        self.pushButton_results.setObjectName(u"pushButton_results")
        self.pushButton_results.setMinimumSize(QSize(25, 150))
        self.pushButton_results.setMaximumSize(QSize(25, 150))
        self.pushButton_results.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_results.setAutoFillBackground(False)
        self.pushButton_results.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton_results.setAutoRepeat(False)
        self.pushButton_results.setAutoExclusive(False)
        self.pushButton_results.setAutoDefault(False)
        self.pushButton_results.setFlat(False)

        self.verticalLayout_4.addWidget(self.pushButton_results)

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
        self.label.setGeometry(QRect(20, 240, 181, 31))
        self.label.setStyleSheet(u"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 0, 181, 31))
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
        self.radioButton_8bit.setGeometry(QRect(90, 440, 63, 15))
        self.radioButton_8bit.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";")
        self.radioButton_16bit = QRadioButton(self.frame_6)
        self.radioButton_16bit.setObjectName(u"radioButton_16bit")
        self.radioButton_16bit.setGeometry(QRect(150, 440, 61, 16))
        self.radioButton_16bit.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";")
        self.label_lowerGrip_2 = QLabel(self.frame_6)
        self.label_lowerGrip_2.setObjectName(u"label_lowerGrip_2")
        self.label_lowerGrip_2.setGeometry(QRect(10, 435, 71, 20))
        self.label_lowerGrip_2.setStyleSheet(u"QLabel{\n"
"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"border:none;\n"
"}")
        self.checkBox = QCheckBox(self.frame_6)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 470, 91, 13))
        self.checkBox.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"font: 87 8pt \"Segoe UI Black\";")
        self.label_upperGrip = QLabel(self.frame_6)
        self.label_upperGrip.setObjectName(u"label_upperGrip")
        self.label_upperGrip.setGeometry(QRect(110, 500, 101, 22))
        self.label_upperGrip.setStyleSheet(u"QLabel{\n"
"color: rgb(200, 200, 200);\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"border:none;\n"
"}")
        self.label_lowerGrip = QLabel(self.frame_6)
        self.label_lowerGrip.setObjectName(u"label_lowerGrip")
        self.label_lowerGrip.setGeometry(QRect(10, 500, 101, 22))
        self.label_lowerGrip.setStyleSheet(u"QLabel{\n"
"color: rgb(200, 200, 200);\n"
"font: 87 8pt \"Segoe UI Black\";\n"
"border:none;\n"
"}")
        self.line_4 = QFrame(self.frame_6)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(10, 410, 200, 3))
        self.line_4.setStyleSheet(u"background-color: rgb(100, 100, 100);")
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 380, 181, 21))
        self.label_6.setStyleSheet(u"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.frame_lut = QFrame(self.frame_6)
        self.frame_lut.setObjectName(u"frame_lut")
        self.frame_lut.setGeometry(QRect(50, 540, 110, 110))
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
        self.verticalLayout_11 = QVBoxLayout(self.page_2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.page_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"border-bottom-left-radius: 115px;")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.label_11 = QLabel(self.frame_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 0, 181, 31))
        self.label_11.setStyleSheet(u"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.line_6 = QFrame(self.frame_10)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(10, 30, 200, 3))
        self.line_6.setStyleSheet(u"background-color: rgb(100, 100, 100);")
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.pushButton_experimentStart = QPushButton(self.frame_10)
        self.pushButton_experimentStart.setObjectName(u"pushButton_experimentStart")
        self.pushButton_experimentStart.setGeometry(QRect(60, 410, 100, 30))
        self.pushButton_experimentStart.setMinimumSize(QSize(100, 30))
        self.pushButton_experimentStart.setMaximumSize(QSize(100, 30))
        self.pushButton_experimentStart.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_experimentStart.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/icons/icons/start.png);\n"
"background-color: rgba(150, 150, 150,100);\n"
"border-radius:12px;\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(0, 130, 0);\n"
"border-radius:12px;\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}")
        self.label_12 = QLabel(self.frame_10)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 270, 111, 20))
        self.label_12.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";")
        self.line_9 = QFrame(self.frame_10)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(10, 290, 150, 1))
        self.line_9.setStyleSheet(u"background-color: rgb(100, 100, 100);")
        self.line_9.setLineWidth(2)
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)
        self.layoutWidget = QWidget(self.frame_10)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 350, 201, 32))
        self.gridLayout_3 = QGridLayout(self.layoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";")
        self.label_13.setFrameShape(QFrame.NoFrame)

        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)

        self.lineEdit_zstack_zstackStart_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_zstack_zstackStart_2.setObjectName(u"lineEdit_zstack_zstackStart_2")
        self.lineEdit_zstack_zstackStart_2.setMinimumSize(QSize(60, 30))
        self.lineEdit_zstack_zstackStart_2.setMaximumSize(QSize(60, 30))
        self.lineEdit_zstack_zstackStart_2.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_zstack_zstackStart_2.setStyleSheet(u"QLineEdit{\n"
"color: rgb(0,0, 0);\n"
"	font: 63 8pt \"Segoe UI Semibold\";\n"
"background-color:rgb(250, 250, 250);\n"
"border-radius:3px;\n"
"\n"
"}\n"
"")
        self.lineEdit_zstack_zstackStart_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lineEdit_zstack_zstackStart_2, 0, 1, 1, 1)

        self.layoutWidget_3 = QWidget(self.frame_10)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 90, 201, 32))
        self.gridLayout_5 = QGridLayout(self.layoutWidget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.layoutWidget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";")
        self.label_15.setFrameShape(QFrame.NoFrame)

        self.gridLayout_5.addWidget(self.label_15, 0, 0, 1, 1)

        self.lineEdit_zstack_zstackStart_4 = QLineEdit(self.layoutWidget_3)
        self.lineEdit_zstack_zstackStart_4.setObjectName(u"lineEdit_zstack_zstackStart_4")
        self.lineEdit_zstack_zstackStart_4.setMinimumSize(QSize(100, 30))
        self.lineEdit_zstack_zstackStart_4.setMaximumSize(QSize(100, 30))
        self.lineEdit_zstack_zstackStart_4.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_zstack_zstackStart_4.setStyleSheet(u"QLineEdit{\n"
"color: rgb(0,0, 0);\n"
"	font: 63 8pt \"Segoe UI Semibold\";\n"
"background-color:rgb(250, 250, 250);\n"
"border-radius:3px;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.lineEdit_zstack_zstackStart_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lineEdit_zstack_zstackStart_4, 0, 1, 1, 1)

        self.label_16 = QLabel(self.frame_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 50, 111, 20))
        self.label_16.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";")
        self.line_10 = QFrame(self.frame_10)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(10, 70, 150, 1))
        self.line_10.setStyleSheet(u"background-color: rgb(100, 100, 100);")
        self.line_10.setLineWidth(2)
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)
        self.widget = QWidget(self.frame_10)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 310, 201, 32))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";")
        self.label_7.setFrameShape(QFrame.NoFrame)

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.lineEdit_zstack_zstackStart = QLineEdit(self.widget)
        self.lineEdit_zstack_zstackStart.setObjectName(u"lineEdit_zstack_zstackStart")
        self.lineEdit_zstack_zstackStart.setMinimumSize(QSize(60, 30))
        self.lineEdit_zstack_zstackStart.setMaximumSize(QSize(60, 30))
        self.lineEdit_zstack_zstackStart.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_zstack_zstackStart.setStyleSheet(u"QLineEdit{\n"
"color: rgb(0,0, 0);\n"
"	font: 63 8pt \"Segoe UI Semibold\";\n"
"background-color:rgb(250, 250, 250);\n"
"border-radius:3px;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.lineEdit_zstack_zstackStart.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lineEdit_zstack_zstackStart, 0, 1, 1, 1)

        self.widget1 = QWidget(self.frame_10)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 130, 201, 121))
        self.gridLayout_4 = QGridLayout(self.widget1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.widget1)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";")
        self.label_14.setFrameShape(QFrame.NoFrame)

        self.gridLayout_4.addWidget(self.label_14, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.widget1)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(100, 100))
        self.plainTextEdit.setMaximumSize(QSize(100, 100))
        self.plainTextEdit.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit{\n"
"color: rgb(0,0, 0);\n"
"font: 63 8pt \"Segoe UI Semibold\";\n"
"background-color:rgb(250, 250, 250);\n"
"border-radius:3px;\n"
"\n"
"}\n"
"\n"
"")
        self.plainTextEdit.setFrameShape(QFrame.NoFrame)

        self.gridLayout_4.addWidget(self.plainTextEdit, 0, 1, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.page_2)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_10 = QVBoxLayout(self.page_7)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.page_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"border-bottom-left-radius: 115px;")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 0, 181, 31))
        self.label_8.setStyleSheet(u"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.line_5 = QFrame(self.frame_9)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(10, 30, 200, 3))
        self.line_5.setStyleSheet(u"background-color: rgb(100, 100, 100);")
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.stackedWidget_results = QStackedWidget(self.frame_9)
        self.stackedWidget_results.setObjectName(u"stackedWidget_results")
        self.stackedWidget_results.setGeometry(QRect(10, 60, 200, 300))
        self.stackedWidget_results.setMinimumSize(QSize(200, 300))
        self.stackedWidget_results.setMaximumSize(QSize(16777215, 300))
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.label_9 = QLabel(self.page_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 10, 111, 20))
        self.label_9.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";")
        self.pushButton_cap_2 = QPushButton(self.page_8)
        self.pushButton_cap_2.setObjectName(u"pushButton_cap_2")
        self.pushButton_cap_2.setGeometry(QRect(60, 210, 80, 30))
        self.pushButton_cap_2.setMinimumSize(QSize(80, 30))
        self.pushButton_cap_2.setMaximumSize(QSize(80, 30))
        self.pushButton_cap_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_cap_2.setStyleSheet(u"QPushButton{\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
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
        self.label_10 = QLabel(self.page_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 130, 111, 20))
        self.label_10.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";")
        self.comboBox_saveDataResolution = QComboBox(self.page_8)
        self.comboBox_saveDataResolution.addItem("")
        self.comboBox_saveDataResolution.addItem("")
        self.comboBox_saveDataResolution.addItem("")
        self.comboBox_saveDataResolution.addItem("")
        self.comboBox_saveDataResolution.setObjectName(u"comboBox_saveDataResolution")
        self.comboBox_saveDataResolution.setGeometry(QRect(30, 160, 150, 25))
        self.comboBox_saveDataResolution.setMinimumSize(QSize(150, 25))
        self.comboBox_saveDataResolution.setMaximumSize(QSize(150, 25))
        self.comboBox_saveDataResolution.setLayoutDirection(Qt.LeftToRight)
        self.comboBox_saveDataResolution.setStyleSheet(u"QComboBox{\n"
"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"border-radius:2px;\n"
"border-none;\n"
"background-color: transparent;\n"
"}\n"
"QComboBox QAbstractItemView{border: 0px;color:white}")
        self.line_7 = QFrame(self.page_8)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(10, 30, 150, 1))
        self.line_7.setStyleSheet(u"background-color: rgb(100, 100, 100);")
        self.line_7.setLineWidth(2)
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.line_8 = QFrame(self.page_8)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(10, 150, 150, 1))
        self.line_8.setStyleSheet(u"background-color: rgb(100, 100, 100);")
        self.line_8.setLineWidth(2)
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.widget2 = QWidget(self.page_8)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(20, 40, 151, 71))
        self.gridLayout = QGridLayout(self.widget2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_lowerGrip_6 = QLabel(self.widget2)
        self.label_lowerGrip_6.setObjectName(u"label_lowerGrip_6")
        self.label_lowerGrip_6.setStyleSheet(u"QLabel{\n"
"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"border:none;\n"
"}")

        self.gridLayout.addWidget(self.label_lowerGrip_6, 0, 0, 1, 1)

        self.frame_result8bit = QFrame(self.widget2)
        self.frame_result8bit.setObjectName(u"frame_result8bit")
        self.frame_result8bit.setMinimumSize(QSize(60, 30))
        self.frame_result8bit.setMaximumSize(QSize(60, 30))
        self.frame_result8bit.setStyleSheet(u"\n"
"border-radius:none;")
        self.frame_result8bit.setFrameShape(QFrame.NoFrame)
        self.frame_result8bit.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_result8bit, 0, 1, 1, 1)

        self.label_lowerGrip_7 = QLabel(self.widget2)
        self.label_lowerGrip_7.setObjectName(u"label_lowerGrip_7")
        self.label_lowerGrip_7.setStyleSheet(u"QLabel{\n"
"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";\n"
"border:none;\n"
"}")

        self.gridLayout.addWidget(self.label_lowerGrip_7, 1, 0, 1, 1)

        self.frame_results16bit = QFrame(self.widget2)
        self.frame_results16bit.setObjectName(u"frame_results16bit")
        self.frame_results16bit.setMinimumSize(QSize(60, 30))
        self.frame_results16bit.setMaximumSize(QSize(60, 30))
        self.frame_results16bit.setStyleSheet(u"\n"
"border-radius:none;")
        self.frame_results16bit.setFrameShape(QFrame.NoFrame)
        self.frame_results16bit.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.frame_results16bit, 1, 1, 1, 1)

        self.stackedWidget_results.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.label_87 = QLabel(self.page_9)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setGeometry(QRect(10, 20, 120, 30))
        self.label_87.setMinimumSize(QSize(120, 30))
        self.label_87.setMaximumSize(QSize(120, 30))
        self.label_87.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";")
        self.progressBar = QProgressBar(self.page_9)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 60, 171, 23))
        self.progressBar.setStyleSheet(u"QProgressBar\n"
"{\n"
"    background: rgb(100, 100, 100);\n"
"    text-align: center;\n"
"	color: rgb(0, 0,170);\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: rgb(200, 200,200)\n"
"}")
        self.progressBar.setValue(24)
        self.pushButton_cancelSaving = QPushButton(self.page_9)
        self.pushButton_cancelSaving.setObjectName(u"pushButton_cancelSaving")
        self.pushButton_cancelSaving.setGeometry(QRect(50, 100, 80, 30))
        self.pushButton_cancelSaving.setMinimumSize(QSize(80, 30))
        self.pushButton_cancelSaving.setMaximumSize(QSize(80, 30))
        self.pushButton_cancelSaving.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_cancelSaving.setStyleSheet(u"QPushButton{\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
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
        self.stackedWidget_results.addWidget(self.page_9)

        self.verticalLayout_10.addWidget(self.frame_9)

        self.stackedWidget.addWidget(self.page_7)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_5.addWidget(self.frame_3, 0, Qt.AlignTop)


        self.horizontalLayout_4.addWidget(self.frame_rightMenu)


        self.verticalLayout_12.addWidget(self.frame_scaffold)

        self.stackedWidget_mainPage.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.verticalLayout_13 = QVBoxLayout(self.page_11)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.page_11)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(250, 500))
        self.frame_12.setMaximumSize(QSize(250, 500))
        self.frame_12.setStyleSheet(u"background-color: rgb(40, 40, 40);\n"
"border-bottom-right-radius: 115px;\n"
"border-top-right-radius: 115px;")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.label_17 = QLabel(self.frame_12)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 130, 181, 20))
        self.label_17.setStyleSheet(u"color: rgb(200, 200, 200);\n"
"font: 87 9pt \"Segoe UI Black\";")
        self.label_18 = QLabel(self.frame_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(20, 80, 181, 31))
        self.label_18.setStyleSheet(u"font: 87 12pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.frame_progress = QFrame(self.frame_12)
        self.frame_progress.setObjectName(u"frame_progress")
        self.frame_progress.setGeometry(QRect(60, 170, 110, 110))
        self.frame_progress.setMinimumSize(QSize(110, 110))
        self.frame_progress.setMaximumSize(QSize(110, 110))
        self.frame_progress.setFrameShape(QFrame.NoFrame)
        self.frame_progress.setFrameShadow(QFrame.Raised)
        self.frame_33 = QFrame(self.frame_progress)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setGeometry(QRect(30, 30, 50, 50))
        self.frame_33.setMinimumSize(QSize(50, 50))
        self.frame_33.setMaximumSize(QSize(50, 50))
        self.frame_33.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"border-radius :25px;")
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.line_11 = QFrame(self.frame_12)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(10, 110, 220, 3))
        self.line_11.setStyleSheet(u"background-color: rgb(100, 100, 100);")
        self.line_11.setLineWidth(2)
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)
        self.pushButton_finishProgress = QPushButton(self.frame_12)
        self.pushButton_finishProgress.setObjectName(u"pushButton_finishProgress")
        self.pushButton_finishProgress.setGeometry(QRect(130, 310, 80, 30))
        self.pushButton_finishProgress.setMinimumSize(QSize(80, 30))
        self.pushButton_finishProgress.setMaximumSize(QSize(80, 30))
        self.pushButton_finishProgress.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_finishProgress.setStyleSheet(u"QPushButton{\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
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
        self.pushButton_cancelProgress = QPushButton(self.frame_12)
        self.pushButton_cancelProgress.setObjectName(u"pushButton_cancelProgress")
        self.pushButton_cancelProgress.setGeometry(QRect(20, 310, 80, 30))
        self.pushButton_cancelProgress.setMinimumSize(QSize(80, 30))
        self.pushButton_cancelProgress.setMaximumSize(QSize(80, 30))
        self.pushButton_cancelProgress.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_cancelProgress.setStyleSheet(u"QPushButton{\n"
"font: 63 10pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(150, 150, 150,100);\n"
"border-radius:15px;\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(130, 0, 0);\n"
"border-radius:15px;\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}")

        self.horizontalLayout_11.addWidget(self.frame_12, 0, Qt.AlignVCenter)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_13)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.pictureBox_progress = QtImageViewer_preview()
        self.pictureBox_progress.setObjectName(u"pictureBox_progress")
        sizePolicy.setHeightForWidth(self.pictureBox_progress.sizePolicy().hasHeightForWidth())
        self.pictureBox_progress.setSizePolicy(sizePolicy)
        self.pictureBox_progress.setMinimumSize(QSize(535, 0))
        self.pictureBox_progress.setMaximumSize(QSize(16777215, 16777215))
        self.pictureBox_progress.setMouseTracking(False)
        self.pictureBox_progress.setStyleSheet(u"QGraphicsView{\n"
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
        self.pictureBox_progress.setFrameShape(QFrame.NoFrame)
        self.pictureBox_progress.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.pictureBox_progress)


        self.horizontalLayout_11.addWidget(self.frame_13)


        self.verticalLayout_13.addWidget(self.frame_11)

        self.stackedWidget_mainPage.addWidget(self.page_11)

        self.verticalLayout.addWidget(self.stackedWidget_mainPage)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_minimize.setDefault(False)
        self.pushButton_maximize.setDefault(False)
        self.pushButton_exit.setDefault(False)
        self.stackedWidget_mainPage.setCurrentIndex(0)
        self.stackedWidget_camera.setCurrentIndex(1)
        self.stackedWidget_bottom.setCurrentIndex(1)
        self.pushButton_preview.setDefault(False)
        self.pushButton_video.setDefault(False)
        self.pushButton_results.setDefault(False)
        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_results.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.pushButton_minimize.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_maximize.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_exit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_exit.setText("")
        self.label_lowerGrip_3.setText(QCoreApplication.translate("MainWindow", u"Bit Depth : ", None))
        self.pushButton_cap.setText("")
        self.label_lowerGrip_4.setText(QCoreApplication.translate("MainWindow", u"8 Bit ", None))
        self.label_lowerGrip_5.setText(QCoreApplication.translate("MainWindow", u"16 bit", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.pushButton_resultCaptureLeft.setText("")
        self.pushButton_resultCaptureRight.setText("")
        self.label_resultCaptureIndex.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.pushButton_preview.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_preview.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_video.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_video.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_results.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_results.setText("")
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
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Experiment", None))
        self.pushButton_experimentStart.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Parameters  : ", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Delay (ms) :", None))
        self.lineEdit_zstack_zstackStart_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Project Name :", None))
        self.lineEdit_zstack_zstackStart_4.setText(QCoreApplication.translate("MainWindow", u"Test_1", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Project :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Captures :", None))
        self.lineEdit_zstack_zstackStart.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Description :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Data Save", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Data  : ", None))
        self.pushButton_cap_2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Resolution  : ", None))
        self.comboBox_saveDataResolution.setItemText(0, QCoreApplication.translate("MainWindow", u"3840 x 2160", None))
        self.comboBox_saveDataResolution.setItemText(1, QCoreApplication.translate("MainWindow", u"2560 x 1440", None))
        self.comboBox_saveDataResolution.setItemText(2, QCoreApplication.translate("MainWindow", u"1920 x 1080", None))
        self.comboBox_saveDataResolution.setItemText(3, QCoreApplication.translate("MainWindow", u"1280 x 720", None))

        self.comboBox_saveDataResolution.setCurrentText(QCoreApplication.translate("MainWindow", u"3840 x 2160", None))
        self.label_lowerGrip_6.setText(QCoreApplication.translate("MainWindow", u"8 Bit :", None))
        self.label_lowerGrip_7.setText(QCoreApplication.translate("MainWindow", u"16 bit : ", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Data Saving :", None))
        self.pushButton_cancelSaving.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Progress :", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Processing", None))
        self.pushButton_finishProgress.setText(QCoreApplication.translate("MainWindow", u"Finish", None))
        self.pushButton_cancelProgress.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
    # retranslateUi

