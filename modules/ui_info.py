# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'infolmoThv.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_Dialog_info(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(300, 200)
        Dialog.setMinimumSize(QSize(300, 200))
        Dialog.setMaximumSize(QSize(300, 200))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.container = QFrame(Dialog)
        self.container.setObjectName(u"container")
        self.container.setStyleSheet(u"")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.container)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.frame_title = QFrame(self.container)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMinimumSize(QSize(0, 40))
        self.frame_title.setMaximumSize(QSize(16777215, 40))
        self.frame_title.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"")
        self.frame_title.setFrameShape(QFrame.NoFrame)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_title)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_title)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgba(0, 122, 204,100);\n"
"font: 63 14pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-radius:none;\n"
"\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_4.addWidget(self.frame_title)

        self.frame_2 = QFrame(self.container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_main = QFrame(self.frame_2)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.frame_3 = QFrame(self.frame_main)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_info = QTextBrowser(self.frame_3)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setStyleSheet(u"QTextBrowser{\n"
"font: 63 12pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"}\n"
"\n"
"QScrollBar:horizontal\n"
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
"     border-image:"
                        " url(:/qss_icons/rc/left_arrow_disabled.png);\n"
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
" QScrollB"
                        "ar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
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
"     borde"
                        "r-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
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
" QSc"
                        "rollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"\n"
" {\n"
"\n"
"     background: none;\n"
"\n"
" }")

        self.horizontalLayout_3.addWidget(self.label_info)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_main)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_close = QPushButton(self.frame_4)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setMinimumSize(QSize(80, 30))
        self.pushButton_close.setMaximumSize(QSize(80, 30))
        self.pushButton_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_close.setStyleSheet(u"QPushButton{\n"
"font: 63 11pt \"Segoe UI Semibold\";\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"background-color: rgba(150, 150, 150,100);\n"
"border-radius:4px;\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(170, 0, 0);\n"
"border-radius:4px;\n"
"border:none;\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_close)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.frame_main)


        self.verticalLayout_4.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.container)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"INFO", None))
        self.label_info.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semibold'; font-size:12pt; font-weight:56; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_close.setText(QCoreApplication.translate("Dialog", u"Close", None))
    # retranslateUi

