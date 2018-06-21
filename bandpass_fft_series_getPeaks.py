# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 23:04:41 2018

@author: fengh
"""

# creating butter bandpass filter
def butter_bandpass_filter(data, lowcut, highcut, fs, order):
    from scipy.signal import butter, lfilter
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    cleanData = lfilter(b, a, data)
    return cleanData
# define a function which reads the audio file and do the FFT
def doFFT(waveData, Fs):
    # import libs for future usage
    import numpy as np
    # import matplotlib.pyplot as plt
    # Fs = 44100.0
    # import scipy as sp
    # read file
    # waveData, Fs = sf.read(filteredData)
    # get the file/FFT length which means the total frames for the file
    waveData = waveData[:, 0]
    N = len(waveData)
    FFTData = np.fft.rfft(waveData)
    p2 = np.abs(FFTData / N)
    p2 = np.array([p2])
    gain = 2 * p2[0, 0:int(N / 2)]
    Range = np.linspace(0, int(N / 2), int(N / 2))
    Range.shape
    freqRan = Fs*Range/N
    # combine freqRan and Gain to dictionary type file for future usage
    freqData = {'frequency' : freqRan, 'gain' : gain}
    return freqData

def findPeak(freqData):
    import pandas as pd
    import matplotlib.pyplot as plt
    import scipy
    import numpy as np
    df = pd.DataFrame(freqData)
    low = 50
    high = 350
    # make sure change the frequency range when instrument changes
    #df = df[(df['frequency'] >= 1000) & (df['frequency'] <= 2250)]
    df = df[(df['frequency'] >= low) & (df['frequency'] <= high)]
    df = df.reset_index(drop=True)
    plt.figure(2)
    plt.plot(df.frequency, df.gain)
    # peakind = scipy.signal.find_peaks_cwt(df.gain, np.arange(1, 3500))
    # hot to get 380 this value:
    # 50/(400-50) = x/total len(df)
    window = 50 * len(df)/(high - low)
    peakind = scipy.signal.find_peaks_cwt(df.gain, np.arange(1, window))
    notes = df.frequency[peakind]
    return notes

# main testing code
import soundfile as sf
# import scipy as sp
# read file
# file = r'D:\LabWork\ThesisProject\noteDetection\c.wav'
# testing new xylophone sound clip
# signal not very clear to me, may need think more
file = r'D:\Howard_Feng\noteDetection\c.wav'
# no difference between 48k and 44k hz as fs
# file = r'D:\Howard_Feng\noteDetection\guitar2.wav'
waveData, fs = sf.read(file)
# Sample rate and desired cutoff frequencies (in Hz).
# need to change the cutoff frequency, new xylophone is different from before
# that is one of the reason cannot get proper result
lowcut = 50.0
highcut = 500.0
#lowcut = 1000.0
#highcut = 2250.0
y = butter_bandpass_filter(waveData, lowcut, highcut, fs, order=3)
freqData = doFFT(y, fs)
# call find peak function return peak frequency
peak = findPeak(freqData)
