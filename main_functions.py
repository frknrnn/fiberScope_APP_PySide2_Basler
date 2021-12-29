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
from infoFunctions import infoPage
from datetime import datetime
import threading
import os
from skimage import io
import cv2
import serial
import time
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

        self.ui.pushButton_preview.clicked.connect(self.showPreview)
        self.ui.pushButton_video.clicked.connect(self.showVideo)
        self.ui.pushButton_results.clicked.connect(self.showResults)


        self.ui.radioButton_8bit.toggled.connect(self.show_8_16_bit_Preview)
        self.ui.radioButton_16bit.toggled.connect(self.show_8_16_bit_Preview)
        self.ui.checkBox.stateChanged.connect(self.lut_state_changed)

        self.ui.pushButton_quickExposure.clicked.connect(self.quickSetExposure)
        self.ui.pushButton_quickGain.clicked.connect(self.quickSetGain)

        self.ui.pushButton_resultCaptureLeft.clicked.connect(self.previous_capture)
        self.ui.pushButton_resultCaptureRight.clicked.connect(self.next_capture)

        self.ui.pushButton_cap.clicked.connect(self.quickTakeCap)

        self.createCustomWidgets()
        self.startCam(1280, 960, 0)
        self.ui.radioButton_8bit.toggle()
        self.bitMode = "8 bit"

        self.windowStatus = 0

        self.cam.setExposure(0.001)

        self.initialSettings()

        def moveWindow(event):
            if(self.windowStatus==0):
                # IF LEFT CLICK MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()

        self.ui.frame_tabBar.mouseMoveEvent=moveWindow

    def initialSettings(self):
        self.maxCapture = 100
        self.noAvailableExperiment = False
        self.ui.stackedWidget_mainPage.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget_bottom.setCurrentIndex(0)
        self.ui.stackedWidget_results.setCurrentIndex(0)
        self.ui.stackedWidget_camera.setCurrentIndex(0)


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

        self.bit16Layout = QVBoxLayout(self.ui.frame_16bit)
        self.bit16Flag = PyToggle()
        self.bit16Layout.addWidget(self.bit16Flag, Qt.AlignCenter, Qt.AlignCenter)

        self.bit8Layout = QVBoxLayout(self.ui.frame_8bit)
        self.bit8Flag = PyToggle()
        self.bit8Layout.addWidget(self.bit8Flag, Qt.AlignCenter, Qt.AlignCenter)

        self.result16bitLayout = QVBoxLayout(self.ui.frame_results16bit)
        self.result16bitFlag = PyToggle()
        self.result16bitLayout.addWidget(self.result16bitFlag, Qt.AlignCenter, Qt.AlignCenter)

        self.result8bitLayout = QVBoxLayout(self.ui.frame_result8bit)
        self.result8bitFlag = PyToggle()
        self.result8bitLayout.addWidget(self.result8bitFlag, Qt.AlignCenter, Qt.AlignCenter)

        self.slider_captures = PySlider(bg_size=14,
                                        bg_radius=7,
                                        handle_size=10,
                                        handle_radius=5,
                                        bg_color="#c8c8c8",
                                        bg_color_hover="#969696",
                                        )
        self.slider_captures.setOrientation(Qt.Horizontal)
        self.slider_captures.setMinimumWidth(250)
        self.slider_captures.valueChanged.connect(self.changeCaptureSliderIndex)
        self.layout_captures = QVBoxLayout(self.ui.frame_resultCaptureSlider)
        self.layout_captures.addWidget(self.slider_captures, Qt.AlignCenter, Qt.AlignCenter)

    def changeCaptureSliderIndex(self):
        self.currentCaptureIndex = self.slider_captures.value()
        self.ui.label_resultCaptureIndex.setText(str(self.currentCaptureIndex))

    def next_capture(self):
        index = self.slider_captures.value()
        if(index<self.maxCapture-1):
            index+=1
        self.slider_captures.setValue(index)

    def previous_capture(self):
        index = self.slider_captures.value()
        if(index>0):
            index-=1
        self.slider_captures.setValue(index)


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



    def quickTakeCap(self):

        if(self.bit8Flag.isChecked() !=True and self.bit16Flag.isChecked() !=True):
            self.infoPage = infoPage()
            self.infoPage.loading_ui.label_info.setText("Please select the pixel format.")
            return
        self.cam.real_mode_deactive()

        folderPath = QFileDialog.getExistingDirectory(self, 'Select folder')
        if(folderPath==""):
            print("cancel Folder")
            return

        date_object = datetime.now()
        date_object = date_object.strftime("%Y_%m_%d_%H_%M")
        directory = folderPath +"/"+ str(date_object)+"_Cap"


        if not os.path.exists(directory):
            os.makedirs(directory)

        self.quickDirectory = directory

        self.infoPage = infoPage()
        self.infoPage.loading_ui.label_info.setText("Captured.")
        self.infoPage.loading_ui.pushButton_close.hide()
        x = threading.Thread(target=self.takeCapImages)
        x.start()

    def takeCapImages(self):

        directory = self.quickDirectory
        cap_image = self.cam.takeCap()
        if (self.bit16Flag.isChecked()):
            dirr_w16 = directory + "/cap_16.tif"
            io.imsave(dirr_w16, cap_image)
        if (self.bit8Flag.isChecked()):
            w_image_8 = self.bytescaling(cap_image)
            dirr_w8 = directory + "/cap_8.tif"
            io.imsave(dirr_w8, w_image_8)
        self.cam.real_mode_active()
        self.infoPage.loading_ui.pushButton_close.show()

    def bytescaling(self,data, cmin=None, cmax=None, high=255, low=0):
        """
        Converting the input image to uint8 dtype and scaling
        the range to ``(low, high)`` (default 0-255). If the input image already has
        dtype uint8, no scaling is done.
        :param data: 16-bit image data array
        :param cmin: bias scaling of small values (def: data.min())
        :param cmax: bias scaling of large values (def: data.max())
        :param high: scale max value to high. (def: 255)
        :param low: scale min value to low. (def: 0)
        :return: 8-bit image data array
        """
        if data.dtype == np.uint8:
            return data

        if high > 255:
            high = 255
        if low < 0:
            low = 0
        if high < low:
            raise ValueError("`high` should be greater than or equal to `low`.")

        if cmin is None:
            cmin = data.min()
        if cmax is None:
            cmax = data.max()

        cscale = cmax - cmin
        if cscale == 0:
            cscale = 1

        scale = float(high - low) / cscale
        bytedata = (data - cmin) * scale + low
        return (bytedata.clip(low, high) + 0.5).astype(np.uint8)


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

    def showPreview(self):
        self.leftMenuButtonChangeIcon(0)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.stackedWidget_bottom.setCurrentIndex(0)
        self.ui.stackedWidget_camera.setCurrentIndex(0)


    def showVideo(self):
        self.leftMenuButtonChangeIcon(1)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.stackedWidget_bottom.setCurrentIndex(0)
        self.ui.stackedWidget_camera.setCurrentIndex(0)


    def showResults(self):
        if(self.noAvailableExperiment):
            self.infoPage = infoPage()
            self.infoPage.loading_ui.label_info.setText("Please start an experiment.")
        else:
            self.leftMenuButtonChangeIcon(2)
            self.ui.stackedWidget.setCurrentIndex(2)
            self.ui.stackedWidget_bottom.setCurrentIndex(1)
            self.ui.stackedWidget_camera.setCurrentIndex(1)

    def leftMenuButtonChangeIcon(self,index):
        if(index==0):
            self.ui.pushButton_preview.setStyleSheet(u"QPushButton{\n"
                                                     "background-color:rgb(200,200,200);\n"
                                                     "border: none;\n"
                                                     "background-position:center;\n"
                                                     "background-repeat:no-repeat;\n"
                                                     "border-radius:12px;\n"
                                                     "background-image:url(:/icons/icons/preview_n.png);\n"
                                                     "}\n"
                                                     "QPushButton::hover{\n"
                                                     "border: none;\n"
                                                     "background-position:center;\n"
                                                     "background-repeat:no-repeat;\n"
                                                     "}\n"
                                                     )

            self.ui.pushButton_video.setStyleSheet(u"QPushButton{\n"
                                                     "background-color:rgb(100,100,100);\n"
                                                     "border: none;\n"
                                                     "background-position:center;\n"
                                                     "background-repeat:no-repeat;\n"
                                                     "border-radius:12px;\n"
                                                     "background-image:url(:/icons/icons/video.png);\n"
                                                     "}\n"
                                                     "QPushButton::hover{\n"
                                                     "background-color:rgb(200,200,200);\n"
                                                     "border: none;\n"
                                                     "background-position:center;\n"
                                                     "background-repeat:no-repeat;\n"
                                                     "}\n"
                                                     )
            self.ui.pushButton_results.setStyleSheet(u"QPushButton{\n"
                                                   "background-color:rgb(100,100,100);\n"
                                                   "border: none;\n"
                                                   "background-position:center;\n"
                                                   "background-repeat:no-repeat;\n"
                                                   "border-radius:12px;\n"
                                                   "background-image:url(:/icons/icons/results.png);\n"
                                                   "}\n"
                                                   "QPushButton::hover{\n"
                                                   "background-color:rgb(200,200,200);\n"
                                                   "border: none;\n"
                                                   "background-position:center;\n"
                                                   "background-repeat:no-repeat;\n"
                                                   "}\n"
                                                   )
        if(index==1):
            self.ui.pushButton_preview.setStyleSheet(u"QPushButton{\n"
                                                     "background-color:rgb(100,100,100);\n"
                                                     "border: none;\n"
                                                     "background-position:center;\n"
                                                     "background-repeat:no-repeat;\n"
                                                     "border-radius:12px;\n"
                                                     "background-image:url(:/icons/icons/preview_n.png);\n"
                                                     "}\n"
                                                     "QPushButton::hover{\n"
                                                     "background-color:rgb(200,200,200);\n"
                                                     "border: none;\n"
                                                     "background-position:center;\n"
                                                     "background-repeat:no-repeat;\n"
                                                     "}\n"
                                                     )

            self.ui.pushButton_video.setStyleSheet(u"QPushButton{\n"
                                                   "background-color:rgb(200,200,200);\n"
                                                   "border: none;\n"
                                                   "background-position:center;\n"
                                                   "background-repeat:no-repeat;\n"
                                                   "border-radius:12px;\n"
                                                   "background-image:url(:/icons/icons/video.png);\n"
                                                   "}\n"
                                                   "QPushButton::hover{\n"
                                                   "border: none;\n"
                                                   "background-position:center;\n"
                                                   "background-repeat:no-repeat;\n"
                                                   "}\n"
                                                   )
            self.ui.pushButton_results.setStyleSheet(u"QPushButton{\n"
                                                     "background-color:rgb(100,100,100);\n"
                                                     "border: none;\n"
                                                     "background-position:center;\n"
                                                     "background-repeat:no-repeat;\n"
                                                     "border-radius:12px;\n"
                                                     "background-image:url(:/icons/icons/results.png);\n"
                                                     "}\n"
                                                     "QPushButton::hover{\n"
                                                     "background-color:rgb(200,200,200);\n"
                                                     "border: none;\n"
                                                     "background-position:center;\n"
                                                     "background-repeat:no-repeat;\n"
                                                     "}\n"
                                                     )
        if (index == 2):
            self.ui.pushButton_preview.setStyleSheet(u"QPushButton{\n"
                                                     "background-color:rgb(100,100,100);\n"
                                                     "border: none;\n"
                                                     "background-position:center;\n"
                                                     "background-repeat:no-repeat;\n"
                                                     "border-radius:12px;\n"
                                                     "background-image:url(:/icons/icons/preview_n.png);\n"
                                                     "}\n"
                                                     "QPushButton::hover{\n"
                                                     "background-color:rgb(200,200,200);\n"
                                                     "border: none;\n"
                                                     "background-position:center;\n"
                                                     "background-repeat:no-repeat;\n"
                                                     "}\n"
                                                     )

            self.ui.pushButton_video.setStyleSheet(u"QPushButton{\n"
                                                   "background-color:rgb(100,100,100);\n"
                                                   "border: none;\n"
                                                   "background-position:center;\n"
                                                   "background-repeat:no-repeat;\n"
                                                   "border-radius:12px;\n"
                                                   "background-image:url(:/icons/icons/video.png);\n"
                                                   "}\n"
                                                   "QPushButton::hover{\n"
                                                   "background-color:rgb(200,200,200);\n"
                                                   "border: none;\n"
                                                   "background-position:center;\n"
                                                   "background-repeat:no-repeat;\n"
                                                   "}\n"
                                                   )
            self.ui.pushButton_results.setStyleSheet(u"QPushButton{\n"
                                                     "background-color:rgb(200,200,200);\n"
                                                     "border: none;\n"
                                                     "background-position:center;\n"
                                                     "background-repeat:no-repeat;\n"
                                                     "border-radius:12px;\n"
                                                     "background-image:url(:/icons/icons/results.png);\n"
                                                     "}\n"
                                                     "QPushButton::hover{\n"
                                                     "border: none;\n"
                                                     "background-position:center;\n"
                                                     "background-repeat:no-repeat;\n"
                                                     "}\n"
                                                     )



    def APP_EXİT(self):
        sys.exit(self.app.exec_())
        Exit(0)