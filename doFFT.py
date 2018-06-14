# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:01:09 2018

@author: CV_LAB_Howard
"""

# define a function which reads the audio file and do the FFT
def doFFT(fileName):
    
    # import libs for future usage
    import numpy as np
    import soundfile as sf
    # import scipy as sp
    
    # read file
    waveData, Fs = sf.read(fileName)
    # get the file/FFT length which means the total frames for the file
    N = len(waveData)
    # get duration of the waveData
    # t = N / Fs
    # create timevector
    # Ts = 1.0 / Fs
    # Tv = sp.arange(0.0, t/1000, Ts)
    # Tv = np.array([Tv])
    # do FFT
    FFTData = abs(np.fft.rfft(waveData)/N)
    # select half of the data
    halfFFT = FFTData[range(1, int(N/2)+1, 1)]
    # creat the frequency energy
    ampFreq = 2 * halfFFT[range(0, int(N/2), 1)]
    # convert disFreq to actural frequency 
    freq = np.array(range(0, int(N/2), 1)) * Fs / N
    '''
    import matplotlib.pyplot as plt
    # plot the result
    # subplot for wave file
    plt.figure(1)
    plt.subplot(2,1,1)
    plt.plot(waveData, "g")
    plt.xlabel('Time')
    plt.ylabel('Wave Amplitude')
    # subplot for the frequency file
    plt.subplot(2,1,2)
    plt.plot(freq, ampFreq, "r")
    plt.xlabel('Frequency')
    plt.ylabel('Frequency Energy')
    '''
    # return key values for future useage
    ampFreq = np.array([ampFreq])
    maxpos = np.argmax(ampFreq)
    maxFreq = freq[maxpos + 1]
    return Fs, FFTData, freq, ampFreq, maxFreq

file = r'D:\Howard_Feng\noteDetection\xylo\xylophone_akg.wav'
sound = doFFT(file)

