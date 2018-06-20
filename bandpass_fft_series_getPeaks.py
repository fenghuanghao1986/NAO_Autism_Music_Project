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
    df = df[(df['frequency'] >= 50) & (df['frequency'] <= 450)]
    plt.figure(2)
    plt.plot(df.frequency, df.gain)
    return df

# main testing code
import soundfile as sf
# import scipy as sp

# read file
# file = r'D:\LabWork\ThesisProject\noteDetection\new_xylo\Fast Octave + Hit Table.wav'
# testing new xylophone sound clip
# signal not very clear to me, may need think more
file = r'D:\Howard_Feng\noteDetection\guitar2.wav'
# no difference between 48k and 44k hz as fs
# file = r'D:\Howard_Feng\noteDetection\new_xylo\D Cord.wav'
waveData, fs = sf.read(file)
# Sample rate and desired cutoff frequencies (in Hz).
# need to change the cutoff frequency, new xylophone is different from before
# that is one of the reason cannot get proper result
lowcut = 20.0
highcut = 500.0
y = butter_bandpass_filter(waveData, lowcut, highcut, fs, order=3)
a = doFFT(y, fs)























