# ///////////////////////////////////////////////////////////////
# BY: FURKAN EREN
# PROJECT MADE WITH: Qt Designer and PySide2
# V: 1.0.0
# ///////////////////////////////////////////////////////////////
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_main import Ui_MainWindow
import numpy as np
from baslerCamera import basler_cam
from widgets import CircularProgress,PySlider,PyLabel,PyToggle,DocumentsWidget
import cv2
import serial
import sys

class AppFunctions(QMainWindow):
    def __init__(self,app):
        QMainWindow.__init__(self)
        self.app = app
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.center()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.__press_pos = QPoint()
        self.windowFlag=False #False minimize True maximize

        ###################################### BUTTONS ##################
        self.ui.pushButton_minimize.clicked.connect(self.minimize_restore)
        self.ui.pushButton_maximize.clicked.connect(self.maximize_restore)
        self.ui.pushButton_exit.clicked.connect(self.APP_EXİT)

        self.ui.radioButton_8bit.toggled.connect(self.show_8_16_bit_Preview)
        self.ui.radioButton_16bit.toggled.connect(self.show_8_16_bit_Preview)
        self.ui.checkBox.stateChanged.connect(self.lut_state_changed)

        self.ui.pushButton_quickExposure.clicked.connect(self.quickSetExposure)
        self.ui.pushButton_quickGain.clicked.connect(self.quickSetGain)

        self.createCustomWidgets()
        self.startCam(1280, 960, 0)
        self.ui.radioButton_8bit.toggle()
        self.bitMode = "8 bit"

        self.windowStatus = 0

        self.cam.setExposure(0.001)

        def moveWindow(event):
            if(self.windowStatus==0):
                # IF LEFT CLICK MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()

        self.ui.frame_tabBar.mouseMoveEvent=moveWindow

    def startCam(self,width, heıght,camId):
        self.cam = basler_cam()
        self.cam.change_pixmap_signal.connect(self.update_image)
        self.cam.change_pixmap_signal_low.connect(self.update_image_low)
        self.cam.change_signal_maxValue.connect(self.expoControl)
        self.cam.signal_max_min.connect(self.lutControl)
        self.cam.createCamera(width, heıght, camId)
        self.cam.start()

    def expoControl(self,value):
        self.expoMaxValue=value

    def show_8_16_bit_Preview(self):
        rdBtn = self.sender()
        if (rdBtn.isChecked()):
            if(rdBtn.text()=="8 Bit"):
                self.cam.setLowRes()
                self.bitMode = "8 bit"
            else:
                self.cam.setHighRes()
                self.bitMode = "16 bit"

    def lutControl(self, minMax):
        self.ui.label_lowerGrip.setText("Lower Grip: {}".format(minMax[0]))
        self.ui.label_upperGrip.setText("Upper Grip: {}".format(minMax[1]))
        if(self.bitMode=="8 bit"):
            rate = int(round((minMax[1] / 255) * 100))
            self.lutProgress.set_value(rate)
        else:
            rate = int(round((minMax[1] / 65536) * 100))
            self.lutProgress.set_value(rate)


    ##### Preview Show
    def update_image(self,cv_img):
        #img8 = (cv_img / 256).astype('uint8')
        qt_img = self.convert_cv_qt(cv_img)
        self.capture = cv_img
        self.ui.pictureBox_preview.loadImageFromFile(qt_img)
        self.isCamReady = True

        #self.ui.pictureBox.setPixmap(qt_img)


    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        h, w,l= np.array(cv_img).shape
        self.img=cv_img
        bytes_per_line = w
        convert_to_Qt_format = QImage(cv_img.data, w, h, bytes_per_line, QImage.Format_Grayscale8)
        p = convert_to_Qt_format.scaled(3840, 2160, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)  #QPixmap.fromImage(p) or  #p

    def update_image_low(self,cv_img):
        #img8 = (cv_img / 256).astype('uint8')
        qt_img = self.convert_cv_qt_low(cv_img)
        self.capture = cv_img
        self.ui.pictureBox_preview.loadImageFromFile(qt_img)
        self.isCamReady = True
        #self.ui.pictureBox.setPixmap(qt_img)


    def convert_cv_qt_low(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        h, w= np.array(cv_img).shape
        #h, w,l= np.array(cv_img).shape
        self.img=cv_img
        bytes_per_line = w
        convert_to_Qt_format = QImage(cv_img.data, w, h, bytes_per_line, QImage.Format_Grayscale8)
        p = convert_to_Qt_format.scaled(3840, 2160, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)  #QPixmap.fromImage(p) or  #p

    def lut_state_changed(self):
        if (self.ui.checkBox.isChecked()):
            self.cam.autoLut(True)
        else:
            self.cam.autoLut(False)


    def center(self):
        screen = QGuiApplication.screenAt(QCursor().pos())
        fg = self.frameGeometry()
        fg.moveCenter(screen.geometry().center())
        self.move(fg.topLeft())

    #### CREATE CUSTOM WIDGET
    def createCustomWidgets(self):
        self.blueProgress = CircularProgress()
        self.blueProgress.width = 90
        self.blueProgress.height = 90
        self.blueProgress.setFixedSize(self.blueProgress.width, self.blueProgress.height)
        self.blueProgress.move(10, 10)
        self.blueProgress.add_shadow(True)
        self.blueProgress.font_size = 15
        self.blueProgress.text_color = QColor(0, 0, 0)
        self.blueProgress.bg_color = QColor(150, 150, 150, 150)
        self.blueProgress.progress_color = QColor(0, 0, 200, 150)
        self.blueProgress.setParent(self.ui.frame_blue)
        self.blueProgress.show()

        self.slider_blueLed = PySlider(bg_size=14,
                                       bg_radius=7,
                                       handle_size=10,
                                       handle_radius=5,
                                       handle_color="#0000c8",
                                       bg_color="#c8c8c8",
                                       bg_color_hover="#969696",
                                       handle_color_hover="#0000b8",
                                       handle_color_pressed="#0000b4"
                                       )


        self.slider_blueLed.setOrientation(Qt.Horizontal)
        self.slider_blueLed.setMinimumWidth(190)
        self.slider_blueLed.valueChanged.connect(self.blueLed)
        self.layoutBlueLed = QVBoxLayout(self.ui.frame_blueSlider)
        self.layoutBlueLed.addWidget(self.slider_blueLed, Qt.AlignCenter, Qt.AlignCenter)

        self.lutProgress = CircularProgress()
        self.lutProgress.width = 90
        self.lutProgress.height = 90
        self.lutProgress.setFixedSize(self.lutProgress.width, self.lutProgress.height)
        self.lutProgress.move(10, 10)
        self.lutProgress.add_shadow(True)
        self.lutProgress.font_size = 15
        self.lutProgress.text_color = QColor(0, 0, 0)
        self.lutProgress.bg_color = QColor(150, 150, 150, 150)
        self.lutProgress.progress_color = QColor(0, 200, 0, 150)
        self.lutProgress.setParent(self.ui.frame_lut)
        self.lutProgress.show()

    def quickSetExposure(self):
        userExpValue = float(self.ui.lineEdit_quickExposure.text())
        self.cam.setExposure(userExpValue)

    def quickSetGain(self):
        userGainValue = int(self.ui.lineEdit_quickGain.text())
        if (userGainValue > 23):
            userGainValue = 23
        elif (userGainValue < 0):
            userGainValue = 0
        self.cam.setGain(userGainValue)

    def blueLed(self, value):
        self.blueProgress.set_value(value)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


    def minimize_restore(self):
        self.showMinimized()


    def maximize_restore(self):
        if self.windowStatus==0:
            self.showMaximized()
            self.windowStatus = 1

        else:
            self.windowStatus=0
            self.showNormal()
            self.resize(self.width()+1,self.height()+1)

    def APP_EXİT(self):
        sys.exit(self.app.exec_())
        Exit(0)