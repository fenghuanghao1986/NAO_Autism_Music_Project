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

    import matplotlib.pyplot as plt
    # plot the result
    # subplot for wave file
    plt.figure(1)
    plt.subplot(2,1,1)
    # need to figure out how to show the exact time at x axis
    # now it is just showing the frames
    plt.plot(waveData, "g")
    plt.xlabel('Time')
    plt.ylabel('Wave Amplitude')
    # subplot for the frequency file
    plt.subplot(2,1,2)
    plt.plot(freqRan, gain, "r")
    plt.xlabel('Frequency')
    plt.ylabel('Frequency Energy')
    dic = {'frequency' : freqRan, 'gain' : gain}
    import pandas as pd
    df = pd.DataFrame(dic)
    # make sure change the frequency range when instrument changes
    #df = df[(df['frequency'] >= 1000) & (df['frequency'] <= 2250)]
    df = df[(df['frequency'] >= 50) & (df['frequency'] <= 1200)]
    df = df.reset_index(drop=True)
    plt.figure(2)
    plt.plot(df.frequency, df.gain)
    import scipy
    #peakind = scipy.signal.find_peaks_cwt(df.gain, np.arange(1, 3500))
    # hot to get 380 this value:
    # 50/(400-50) = x/total len(df)
    peakind = scipy.signal.find_peaks_cwt(df.gain, np.arange(1, 380))
    notes = df.frequency[peakind]
    return notes

# main testing code
import soundfile as sf
# import scipy as sp

# read file
file = r'D:\LabWork\ThesisProject\noteDetection\c.wav'
# testing new xylophone sound clip
# signal not very clear to me, may need think more
#file = r'D:\Howard_Feng\noteDetection\new_xylo\2 C.wav'
# no difference between 48k and 44k hz as fs
# file = r'D:\Howard_Feng\noteDetection\guitar2.wav'
waveData, fs = sf.read(file)
# Sample rate and desired cutoff frequencies (in Hz).
# need to change the cutoff frequency, new xylophone is different from before
# that is one of the reason cannot get proper result
lowcut = 50.0
highcut = 1200.0
#lowcut = 1000.0
#highcut = 2250.0
y = butter_bandpass_filter(waveData, lowcut, highcut, fs, order=3)
a = doFFT(y, fs)






















