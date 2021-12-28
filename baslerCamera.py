# ///////////////////////////////////////////////////////////////
#
# BY: FURKAN EREN
# PROJECT MADE WITH: Qt Designer and PySide2
# V: 1.0.0

# ///////////////////////////////////////////////////////////////

import sys
import os
import time
import cv2
import threading
import numpy as np
import signal
import json
from PySide2 import  QtCore,QtGui,QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from scipy import ndimage, misc
import pypylon
import pathlib
from pypylon import pylon
from pypylon import genicam
from pypylon import _genicam
from pypylon import _pylon
import cv2
import numpy as np
from skimage import io

pypylon_dir = pathlib.Path(pypylon.__file__).parent
pypylon_dlls = [(str(dll), '.') for dll in pypylon_dir.glob('*.dll')]
pypylon_pyds = [(str(dll), '.') for dll in pypylon_dir.glob('*.pyd')]

_binaries = list()
_binaries.extend(pypylon_dlls)
_binaries.extend(pypylon_pyds)

_pathex = list()
_pathex.append(str(pypylon_dir))

_hiddenimports = list()
_hiddenimports.extend(['pypylon', 'pypylon.pylon', 'pypylon.genicam', 'pypylon._pylon', 'pypylon._genicam'])

# conecting to the first available camera
# 12 bit için Get array kullanılmıycak onun yerine img = np.ndarray(buffer=image.GetBuffer(),shape=(image.GetHeight(), image.GetWidth(), 3),dtype=np.uint16)
#                     cv2.imwrite("12bit.tif",img)
# ayrıca self.converter.OutputPixelFormat = pylon.PixelType_RGB16packed
#         self.converter.OutputBitAlignment = pylon.OutputBitAlignment_LsbAligned olarak düzenlenicek


class basler_cam(QThread):
    signal_max_min = Signal(list)
    change_signal_maxValue = Signal(int)
    change_pixmap_signal = Signal(np.ndarray)
    change_pixmap_signal_low = Signal(np.ndarray)
    change_pixmap_signal_focus = Signal(np.ndarray)
    _running = True
    def createCamera(self,width,heıght,camId):
        self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
        self.camera.Open()
        self.camera.ExposureTime.SetValue(120000)
        self.camera.Gain.SetValue(0)
        #self.camera.Gain.SetValue(5)
        # reset to default config before all other settings
        #self.camera.UserSetSelector = "Default"
        #self.camera.TLParamsLocked = False
        print(self.camera.Width.GetValue())
        print(self.camera.Height.GetValue())
        #self.camera.Width.SetValue(2000)
        #self.camera.OffsetX.SetValue(500)

        #self.camera.Height.SetValue(200)

        # Grabing Continusely (video) with minimal delay
        self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        self.converter = pylon.ImageFormatConverter()
        # converting to opencv bgr format
        self.converter.OutputPixelFormat = pylon.PixelType_Mono16
        self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

        self.converter_lowRes = pylon.ImageFormatConverter()
        self.converter_lowRes.OutputPixelFormat = pylon.PixelType_Mono8
        self.converter_lowRes.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
        self.lowResFlag=True


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


    def setExposure(self,value):
        self.camera.ExposureTime.SetValue(float(value)*1000000)

    def setGain(self,value):
        self.camera.Gain.SetValue(float(value))

    def setRoi(self,width,height,offsetX,offsetY):
        self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
        self.camera.Open()
        #self.camera.ExposureMode.SetValue("ExposureMode_Timed");

        self.camera.ExposureTime.SetValue(30000)
        self.camera.Gain.SetValue(5)
        self.camera.Width.SetValue(width)
        self.camera.Height.SetValue(height)
        self.camera.OffsetX.SetValue(offsetX)
        self.camera.OffsetY.SetValue(offsetY)
        self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        self.converter = pylon.ImageFormatConverter()


        # converting to opencv bgr format
        self.converter.OutputPixelFormat = pylon.PixelType_Mono12
        self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned
        self._running = True

    def real_mode_deactive(self):
        self._running = False
    def real_mode_active(self):
        self._running = True
        self.start()

    def trigCap(self):
        if self.camera.WaitForFrameTriggerReady(200, pylon.TimeoutHandling_ThrowException):
            self.camera.ExecuteSoftwareTrigger()
        time.sleep(0.02)
        grabResult = self.camera.RetrieveResult(0, pylon.TimeoutHandling_Return)


    def takeCap(self):
        grabResult = self.camera.RetrieveResult(5000, pylon.TimeoutHandling_Return)
        if grabResult.GrabSucceeded():
            # Access the image data
            image = self.converter.Convert(grabResult)
            img = np.ndarray(buffer=image.GetBuffer(), shape=(image.GetHeight(), image.GetWidth(), 1),
                             dtype=np.uint16)
            # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = np.array(img).astype(np.uint16)

        return gray

    def capture(self):
        grabResult = self.camera.RetrieveResult(5000, pylon.TimeoutHandling_Return)
        if grabResult.GrabSucceeded():
            # Access the image data
            image = self.converter.Convert(grabResult)
            img = np.ndarray(buffer=image.GetBuffer(), shape=(image.GetHeight(), image.GetWidth(), 1),
                             dtype=np.uint16)
            # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = np.array(img).astype(np.uint16)
        io.imsave("16bit.tif", np.array(gray).astype('uint16'))

    def calculateLutMax_low(self,max_):
        result = int(round(max_/10))
        result = (result*10)+7
        return result
    def calculateLutMax(self,max_):
        result = int(round(max_/3000))
        result = (result*3000)+2000
        return result


    def autoLut(self,state):
        if(state):
            self.autoLutFlag=True
        else:
            self.autoLutFlag=False


    def terminate(self):
        self.camera.Close()
        self._running = False
    def setLowRes(self):
        self.c_max = 255
        self.lowResFlag = True

    def setHighRes(self):
        self.c_max = 65536
        self.lowResFlag = False


    def run(self):
        self.autoLutFlag = False
        if(self.lowResFlag):
            self.c_max = 255
        else:
            self.c_max = 65536
        while self._running:
            if(self.camera.IsGrabbing()):
                grabResult = self.camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
                if grabResult.GrabSucceeded():
                    if(self.lowResFlag):
                        # Access the image data
                        image = self.converter_lowRes.Convert(grabResult)
                        img = image.GetArray()
                        image = ndimage.median_filter(img, size=2)
                        max_ = np.partition(np.array(image).flatten(), -2)[-1]
                        min_ = np.amin(np.array(img))
                        minMax = []
                        minMax.append(min_)
                        minMax.append(max_)
                        if (self.autoLutFlag):
                            self.c_max = self.calculateLutMax_low(max_)
                        final = self.bytescaling(img, cmin=0, cmax=self.c_max)

                        self.signal_max_min.emit(minMax)
                        self.change_signal_maxValue.emit(max_)
                        self.change_pixmap_signal_low.emit(final)

                    else:
                        # Access the image data
                        image = self.converter.Convert(grabResult)
                        img = np.ndarray(buffer=image.GetBuffer(), shape=(image.GetHeight(), image.GetWidth(), 1),
                                         dtype=np.uint16)
                        #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        temp_max_value = np.amax(img)
                        gray = np.array(img).astype(np.uint16)
                        image = ndimage.median_filter(gray, size=2)
                        max_ = np.partition(np.array(image).flatten(), -2)[-1]
                        min_ = np.amin(np.array(gray))
                        if (self.autoLutFlag):
                            self.c_max = self.calculateLutMax(max_)
                        minMax = []
                        minMax.append(min_)
                        minMax.append(max_)
                        #final = gray
                        final = self.bytescaling(gray, cmin=0, cmax=self.c_max)
                        self.signal_max_min.emit(minMax)
                        self.change_pixmap_signal.emit(final)
                        self.change_signal_maxValue.emit(max_)

                grabResult.Release()



