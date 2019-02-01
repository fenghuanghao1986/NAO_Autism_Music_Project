# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 23:47:00 2019

@author: fengh
"""

from pylab import *
import soundfile as sf
# import scipy as sp

file = r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Audio_Detection_Part\new_xylo\ace.wav'
waveData, fs = sf.read(file)
specgram(waveData[:, 1], NFFT=1024*6)
