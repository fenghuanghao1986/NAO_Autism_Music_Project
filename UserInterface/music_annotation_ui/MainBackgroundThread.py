# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 17:49:40 2019

@author: CV_LAB_Howard
"""
import sounddevice as sd
import soundfile as sf

class MainBackgroundThread(QThread):
    def __init__(self, keyword, sector):
        QThread.__init__(self)
        self.keyword, self.sector = keyword, sector
    def run(self, filename):
#        main(self.keyword, self.sector)
        data, fs = sf.read(filename, dtype='float32')
        sd.play(data, fs)
        sd.wait()