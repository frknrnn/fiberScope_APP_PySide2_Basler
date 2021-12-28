# ///////////////////////////////////////////////////////////////
#
# BY: FURKAN EREN
# PROJECT MADE WITH: Qt Designer and PySide2
# V: 1.0.0

# ///////////////////////////////////////////////////////////////

from modules import *
from widgets import *
from PySide2 import  QtCore
from PySide2.QtWidgets import *
import json

class infoPage(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.__press_pos = QPoint()
        self.loading_ui = Ui_Dialog_info()
        self.loading_ui.setupUi(self)
        ## REMOVE TİTLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.loading_ui.pushButton_close.clicked.connect(self.close)


        ##DropShadowEffect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 122, 204, 50))
        self.loading_ui.container.setGraphicsEffect(self.shadow)

        self.setModal(True)
        self.show()


        def moveWindow(event):
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()
        self.loading_ui.label.mouseMoveEvent=moveWindow


    def close(self):
        self.hide()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

