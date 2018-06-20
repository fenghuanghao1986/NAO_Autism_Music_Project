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
    '''
    # select half of the data
    halfFFT = FFTData[range(1, int(N/2)+1, 1)]
    # creat the frequency energy
    ampFreq = 2 * halfFFT[range(0, int(N/2), 1)]
    # convert disFreq to actural frequency 
    freq = abs(np.array(range(0, int(N/2), 1)) * Fs / N)
    '''
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
    dic = pd.DataFrame(dic)
    return dic

    ''' this part is for single note detection
    # return key values for future useage
    ampFreq = np.array([ampFreq])
    maxpos = np.argmax(ampFreq)
    maxFreq = freq[maxpos + 1]
    return Fs, FFTData, freq, ampFreq, maxFreq
    '''

# main testing code
import soundfile as sf
# import scipy as sp

# read file
file = r'D:\LabWork\ThesisProject\noteDetection\new_xylo\Fast Octave + Hit Table.wav'
# testing new xylophone sound clip
# signal not very clear to me, may need think more
# file = r'D:\Howard_Feng\noteDetection\new_xylo\D_Cord_44k.wav'
# no difference between 48k and 44k hz as fs
# file = r'D:\Howard_Feng\noteDetection\new_xylo\D Cord.wav'
waveData, fs = sf.read(file)
# Sample rate and desired cutoff frequencies (in Hz).
# need to change the cutoff frequency, new xylophone is different from before
# that is one of the reason cannot get proper result
lowcut = 1000.0
highcut = 2500.0
y = butter_bandpass_filter(waveData, lowcut, highcut, fs, order=6)
a = doFFT(y, fs)
#index = findPeaks(freq)
# data[peakind]
