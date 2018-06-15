# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 15:12:38 2018

@author: CV_LAB_Howard
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


def run():
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.signal import freqz
    import soundfile as sf
    # import scipy as sp
    
    # read file
    file = r'D:\Howard_Feng\noteDetection\xylo\xylophone_akg.wav'
    waveData, fs = sf.read(file)
    # get the file/FFT length which means the total frames for the file
    N = len(waveData)
    # Sample rate and desired cutoff frequencies (in Hz).
    lowcut = 2000.0
    highcut = 4000.0

    # Plot the frequency response for a few different orders.
    plt.figure(1)
    plt.clf()
    for order in [3, 6, 9]:
        b, a = butter_bandpass(lowcut, highcut, fs, order=order)
        w, h = freqz(b, a, worN=2000)
        plt.plot((fs * 0.5 / np.pi) * w, abs(h), label="order = %d" % order)

    plt.plot([0, 0.5 * fs], [np.sqrt(0.5), np.sqrt(0.5)],
             '--', label='sqrt(0.5)')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Gain')
    plt.grid(True)
    plt.legend(loc='best')

    # Filter a noisy signal.
    T = N / fs
    t = np.linspace(0, T, N, endpoint=False)
    plt.figure(2)
    plt.clf()
    plt.plot(t, waveData, label='Sound wave')

    y = butter_bandpass_filter(waveData, lowcut, highcut, fs, order=6)
    plt.plot(t, y, label='Filtered signal (%g Hz)')
    plt.xlabel('time (seconds)')
    plt.hlines([-a, a], 0, T, linestyles='--')
    plt.grid(True)
    plt.axis('tight')
    plt.legend(loc='upper left')

    plt.show()


run()