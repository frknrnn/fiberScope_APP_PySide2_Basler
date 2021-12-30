# ///////////////////////////////////////////////////////////////
#
# BY: FURKAN EREN
# PROJECT MADE WITH: Qt Designer and PySide2
# V: 1.0.0

# ///////////////////////////////////////////////////////////////
import serial.tools.list_ports as port_list

import threading
import sys
from ui_splash import Ui_MainWindow
import serial
from serial.tools import list_ports
from main_functions import AppFunctions
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class SplashScreen(QMainWindow):
    def __init__(self,app):
        QMainWindow.__init__(self)
        self.splash_ui = Ui_MainWindow()
        self.splash_ui.setupUi(self)
        self.__press_pos = QPoint()
        ## REMOVE TİTLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.splash_ui.pushButton_quit.clicked.connect(self.APP_EXİT)
        self.splash_ui.pushButton_connect.clicked.connect(self.openApp)


        ##DropShadowEffect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(40)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,128,60))
        self.splash_ui.frame.setGraphicsEffect(self.shadow)
        self.counter=0
        self.app = app
        serial_list = list_ports.comports()
        for i in serial_list:
            self.splash_ui.comboBox_comPort.addItem(i.device)
        self.windowStatus = 0

        ####Function
        def moveWindow(event):
            if(self.windowStatus==0):
                # IF LEFT CLICK MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()

        self.splash_ui.frame_tab.mouseMoveEvent=moveWindow

        self.show()



    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def openApp(self):
        self.main = AppFunctions(self.app,self.splash_ui.comboBox_comPort.currentText(),int(self.splash_ui.comboBox_baudRate.currentText()))
        self.main.show()
        self.close()


    def APP_EXİT(self):
        sys.exit(self.app.exec_())
        Exit(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen(app)
    sys.exit(app.exec_())