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
# Since the built-in function cwt cannot find peaks properly
# This funiction will detect the raw peaks
# later on, a refine function will be applied, to get real peaks
def findRawPeak(freqData):
    import pandas as pd
    import matplotlib.pyplot as plt
    import scipy
    import numpy as np
    df = pd.DataFrame(freqData)
    low = 1000
    high = 3000
    # make sure change the frequency range when instrument changes
    #df = df[(df['frequency'] >= 1000) & (df['frequency'] <= 2250)]
    df = df[(df['frequency'] >= low) & (df['frequency'] <= high)]
    df = df.reset_index(drop=True)
    plt.figure(2)
    plt.plot(df.frequency, df.gain)
    # peakind = scipy.signal.find_peaks_cwt(df.gain, np.arange(1, 3500))
    # hot to get 380 this value:
    # 50/(400-50) = x/total len(df)
    window = 100 * len(df)/(high - low)
    peakind = scipy.signal.find_peaks_cwt(df.gain, np.arange(1, window))
    rawPeak = df.loc[peakind]
    return rawPeak

# this function is to get real peaks for future analysis
def realPeak(rawPeak):
    import numpy as np
    # since music scales is a 
    ratio = 1.059463
    # for guitar starts from E2 to E5 (82.4068Hz to 659.2251Hz)
    # for xylophone from C6 to F7 (1046.5023Hz to 2793.8259Hz)
    # because of the accuracy problem, we can only compare the detected note 
    # in a certain range using the basic ratio between notes
    notes = {'C6': 1046.5023, 'D6': 1174.6591, 'E6': 1318.5102,
             'F6': 1396.9129, 'G6': 1567.9816, 'A6': 1760.0000,
             'B6': 1975.5332, 'C7': 2093.0046, 'D7': 2349.3181,
             'E7': 2637.0205, 'F7': 2793.8259}
    '''
    rawPeak = np.array(peaks)
    n = np.size(peaks)
    newPeak = []
    for key, note in notes.items():
        # thinking about how to use deque so once I get one
        # it will also delete the first one, make second one to first
        for i in range (0, n):
            if peaks[i] >= note / ratio and peaks[i] <= note * ratio:
                newPeak.append(key)
                continue
            else:
                
    '''
    newPeak = []
    
    return newPeak

# main testing code
import soundfile as sf
# import scipy as sp
# read file
# file = r'D:\LabWork\ThesisProject\noteDetection\new_xy.wav'
# testing new xylophone sound clip
# signal not very clear to me, may need think more
# file = r'D:\Howard_Feng\noteDetection\new_xy.wav'
# no difference between 48k and 44k hz as fs
# file = r'D:\Howard_Feng\noteDetection\guitar2.wav'
file = r'C:\Users\fengh\pythonProject\noteDetection\new_xylo\cc.wav'
waveData, fs = sf.read(file)
# Sample rate and desired cutoff frequencies (in Hz).
# need to change the cutoff frequency, new xylophone is different from before
# that is one of the reason cannot get proper result
lowcut = 1000.0
highcut = 3000.0
# for guitar use 50 and 500
y = butter_bandpass_filter(waveData, lowcut, highcut, fs, order=3)
freqData = doFFT(y, fs)
# call find peak function return peak frequency
rawPeak = findRawPeak(freqData)
# newPeak = realPeak(rawPeak)