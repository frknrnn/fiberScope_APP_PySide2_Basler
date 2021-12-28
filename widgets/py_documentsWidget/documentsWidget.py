from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import numpy as np
import math
class DocumentsWidget(QFrame):
    click_signal = Signal(dict)
    def __init__(self,data):
        QFrame.__init__(self)
        # SET DEFAULT PARAMETERS

        self.setObjectName(u"frame_main")
        self.setGeometry(QRect(10, 370, 230, 80))
        self.setMinimumSize(QSize(240, 80))
        self.setMaximumSize(QSize(240, 80))
        self.setFrameShape(QFrame.NoFrame)
        self.setFrameShadow(QFrame.Raised)
        '''
        self.setStyleSheet(u"QFrame{\n"
                                     "font: 63 11pt \"Segoe UI Semibold\";\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "background-color: rgba(150, 150, 150,100);\n"
                                     "border-radius:4px;\n"
                                     "border:none;\n"
                                     "background-repeat: no-repeat;\n"
                                     "background-position: center;\n"
                                     "}\n"
                                     "QFrame::hover{\n"
                                     "background-color: rgba(100, 100, 100,100);\n"
                                     "border-radius:4px;\n"
                                     "border:none;\n"
                                     "background-repeat: no-repeat;\n"
                                     "background-position: center;\n"
                                     "}")
        '''
        self.horizontalLayout_23 = QHBoxLayout(self)
        self.horizontalLayout_23.setSpacing(10)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_imageDisplay = QLabel(self)
        self.label_imageDisplay.setObjectName(u"label_image")
        self.label_imageDisplay.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_imageDisplay.setMinimumSize(QSize(80, 80))
        self.label_imageDisplay.setMaximumSize(QSize(80, 80))
        self.label_imageDisplay.mousePressEvent = self.clickEvent

        self.sizeMB = self.convert_size(data["documentSize"])
        self.data = data
        self.image = data['previewImage']
        self.path = data["path"]
        self.experiments = data["experiments"]

        self.info = []
        self.info.append(self.path)

        height, width, channels = np.array(self.image).shape
        bytesPerLine = channels * width

        qImg = QImage(self.image.data, width, height, bytesPerLine, QImage.Format_RGB888)
        pixmap01 = QPixmap.fromImage(qImg)
        pixmap_image = QPixmap(pixmap01)

        self.label_imageDisplay.setPixmap(pixmap_image)
        self.label_imageDisplay.setAlignment(Qt.AlignCenter)
        self.label_imageDisplay.setScaledContents(True)
        self.label_imageDisplay.setMinimumSize(1, 1)
        self.label_imageDisplay.show()


        self.horizontalLayout_23.addWidget(self.label_imageDisplay)

        self.frame_text = QFrame(self)
        self.frame_text.setObjectName(u"frame_text")
        self.frame_text.setFrameShape(QFrame.StyledPanel)
        self.frame_text.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_23.addWidget(self.frame_text)

        self.verticalLayout_15 = QVBoxLayout(self.frame_text)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_t1 = QLabel(self.frame_text)
        self.label_t1.setText(str(self.path))
        self.label_t1.setObjectName(u"label_t1")
        self.label_t1.setStyleSheet(u"font: 63 8pt \"Segoe UI Semibold\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border:none;")

        self.verticalLayout_15.addWidget(self.label_t1)

        self.label_t2 = QLabel(self.frame_text)
        self.experiments_text = ""
        if("normal" in self.experiments):
            if(self.experiments["normal"]==True):self.experiments_text = self.experiments_text+"capture,"
        if("zStack" in self.experiments):
            if(self.experiments["zStack"]==True):self.experiments_text = self.experiments_text + "zStack,"
        if("timeSeries" in self.experiments):
            if(self.experiments["timeSeries"]==True):self.experiments_text = self.experiments_text + "timeSeries,"
        if("tiles" in self.experiments):
            if(self.experiments["tiles"]==True):self.experiments_text = self.experiments_text + "tiles,"

        self.label_t2.setText(self.experiments_text)
        self.label_t2.setObjectName(u"label_t2")
        self.label_t2.setStyleSheet(u"font: 63 6pt \"Segoe UI Semibold\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border:none;")
        self.verticalLayout_15.addWidget(self.label_t2)

        self.label_t3 = QLabel(self.frame_text)
        self.label_t3.setText("{}".format(self.sizeMB))
        self.label_t3.setObjectName(u"label_t3")
        self.label_t3.setStyleSheet(u"font: 63 10pt \"Segoe UI Semibold\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "border:none;")
        self.verticalLayout_15.addWidget(self.label_t3)

    def clickEvent(self,event):
        self.click_signal.emit(self.data)

    def convert_size(self,size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])
