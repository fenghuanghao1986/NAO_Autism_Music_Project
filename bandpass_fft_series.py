# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 12:22:45 2018

@author: fengh
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 23:04:41 2018

@author: fengh
"""

# creating butter bandpass filter
def butter_bandpass_filter(data, lowcut, highcut, fs, order=9):
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
    freq = abs(np.array(range(0, int(N/2), 1)) * Fs / N)

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
    plt.plot(freq, ampFreq, "r")
    plt.xlabel('Frequency')
    plt.ylabel('Frequency Energy')
    return ampFreq
    ''' this part is for single note detection
    # return key values for future useage
    ampFreq = np.array([ampFreq])
    maxpos = np.argmax(ampFreq)
    maxFreq = freq[maxpos + 1]
    return Fs, FFTData, freq, ampFreq, maxFreq
    '''
    '''
    from scipy import signal
    import numpy as np
    peakind = signal.find_peaks_cwt(freq, np.arange(1, 1000))
    print(peakind)
    print(freq[peakind])
    return freq[peakind]
    #return ampFreq
    '''
'''
def findPeaks(freq):
    from scipy import signal
    import numpy as np
    peakind = signal.find_peaks_cwt(freq, np.arange(2000, 4000))
    print(peakind)
    return peakind
'''

# main testing code
import soundfile as sf
# import scipy as sp

# read file
file = r'D:\LabWork\ThesisProject\noteDetection\xylo\xylophone_akg.wav'
waveData, fs = sf.read(file)
# Sample rate and desired cutoff frequencies (in Hz).
lowcut = 2000.0
highcut = 4000.0
y = butter_bandpass_filter(waveData, lowcut, highcut, fs, order=6)
freq = doFFT(y, fs)
#index = findPeaks(freq)
# data[peakind]