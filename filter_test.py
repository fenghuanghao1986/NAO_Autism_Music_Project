# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 15:55:03 2018

@author: Howard Feng
"""
from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
# import scipy as sp

# read file
file = r'C:\Users\fengh\pythonProject\noteDetection\xylo\low_c_akg.wav'
waveData, fs = sf.read(file)
# get the file/FFT length which means the total frames for the file
N = len(waveData)
# Sample rate and desired cutoff frequencies (in Hz).
lowcut = 2000.0
highcut = 4000.0

y = butter_bandpass_filter(waveData, lowcut, highcut, fs, order=6)

import soundfile as sf
# import scipy as sp

# read file
# get the file/FFT length which means the total frames for the file
FFTData = abs(np.fft.rfft(y)/N)
halfFFT = FFTData[range(1, int(N/2)+1, 1)]
ampFreq = 2 * halfFFT[range(0, int(N/2), 1)]
freq = np.array(range(0, int(N/2), 1)) * fs / N

# plot the result
# subplot for wave file
plt.figure(1)
plt.subplot(2,1,1)
plt.plot(y, "g")
plt.xlabel('Time')
plt.ylabel('Wave Amplitude')
# subplot for the frequency file
plt.subplot(2,1,2)
plt.plot(freq, ampFreq, "r")
plt.xlabel('Frequency')
plt.ylabel('Frequency Energy')