# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 18:50:01 2019

@author: CV_LAB_Howard
"""

# a test code for stft

from scipy import signal
import matplotlib.pyplot as plt
import soundfile as sf
from bandpass_fft_series_getPeaks import butter_bandpass_filter 
import numpy as np
#
#file = r'D:\Howard_Feng\noteDetection\Audio_Detection_Part\new_xylo\ace.wav'
#
#waveData, fs = sf.read(file)
#
#lowcut = 1000.0
#highcut = 3000.0
#
#y = butter_bandpass_filter(waveData, lowcut, highcut, fs, order=3)
#
#f,t,zxx = signal.stft(y, fs)
#

fs = 10e3
N = 1e5
amp = 2 * np.sqrt(2)
#noise_power = 0.01 * fs / 2
time = np.arange(N) / float(fs)
mod = 500*np.cos(2*np.pi*0.25*time)
carrier = np.sin(2*np.pi*3e3*time + mod)

f, t, Zxx = signal.stft(carrier, fs, nperseg=1000)
plt.plot(mod)
plt.show()
#plt.pcolormesh(t, f, np.abs(Zxx), vmin=0, vmax=amp)
#plt.title('STFT Magnitude')
#plt.ylabel('Frequency [Hz]')
#plt.xlabel('Time [sec]')
#plt.show()

