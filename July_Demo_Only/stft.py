import numpy as np
import time
import numpy.fft as fft
from scipy.io import wavfile as wav
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

def stft(x, Nwin, Nfft=None):

   
    Nfft = Nfft or Nwin
    Nwindows = x.size // Nwin
    # reshape into array `Nwin` wide, and as tall as possible. This is
    # optimized for C-order (row-major) layouts.
    arr = np.reshape(x[:Nwindows * Nwin], (-1, Nwin))
    stft = fft.rfft(arr, Nfft)
    return stft


def stftbins(x, Nwin, Nfft=None, d=1.0):
    
    Nfft = Nfft or Nwin
    Nwindows = x.size // Nwin
    t = np.arange(Nwindows) * (Nwin * d)
    f = fft.rfftfreq(Nfft, d)
    return t, f


def istft(stftArr, Nwin):
   
    arr = fft.irfft(stftArr)[:, :Nwin]
    return np.reshape(arr, -1)

def bandpass_filter(data, lowcut, highcut, fs, order):

    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    cleanData = lfilter(b, a, data)
    return cleanData

def realPeak(rawPeak):

    # since music scales is a 
    # ratio = 1.059463
    # for guitar starts from E2 to E5 (82.4068Hz to 659.2251Hz)
    # for xylophone from C6 to F7 (1046.5023Hz to 2793.8259Hz)
    # because of the accuracy problem, we can only compare the detected note 
    # in a certain range using the basic ratio between notes
    notes = {'1': 1038, '2': 1172, '3': 1316,
             '4': 1389, '5': 1561, '6': 1754,
             '7': 1975, '8': 2084, '9': 2343,
             'a': 2626, 'b': 2785}
    
    #peaks = rawPeak.frequency[rawPeak.gain >= rawPeak.gain.mean()*0.4]
    #peaks = np.array(peaks)
    #print(peaks)
    n = len(rawPeak)
    newPeak = []
    
    # for key, note in notes.items():
        # thinking about how to use deque so once I get one
        # it will also delete the first one, make second one to first
    for i in range (n):
        for key, note in notes.items():
            if rawPeak[i] >= note - 10 and rawPeak[i] <= note + 10:
                newPeak.append(key)
#                print(newPeak)
#                print(i)
                break
            else:
                continue

    return newPeak

def findNotes(stftData, fsRange):
    x = len(stftData)
    y = len(stftData[0])
    
    maxAmp = []
    maxLocal = []
    for i in range(x):
        maxima = stftData[i].max()
        index = 0
        
        for j in range(y):
            if stftData[i][j] == maxima and stftData[i][j] > (100*np.mean(stftData)):
                index = j
                break
            
        maxAmp.append([maxima,index])
            
    
#    plt.plot(maxAmp)
#    plt.show()
    for i in range(x):
        if (i == 0):
            if (maxAmp[i][0] >= maxAmp[i+1][0]):
                maxLocal.append(maxAmp[i])
        elif (i == x-1):
            if (maxAmp[i][0] >= maxAmp[i-1][0]):
                maxLocal.append(maxAmp[i])
        elif (maxAmp[i][0] >= maxAmp[i-1][0]) and (maxAmp[i][0] >= maxAmp[i+1][0]):
            maxLocal.append(maxAmp[i])
    
    rawPeaks = []
    for i in range(len(maxLocal)):
        rawPeaks.append(maxLocal[i][1]*fsRange/y)
#            
    return rawPeaks

#def LevDist(s_peak, s_len, t_peak, t_len):
#    
#    if s_len == 0:
#        return t_len
#    if t_len == 0:
#        return s_len
#    if s_peak[s_len - 1] == t_peak[t_len - 1]:
#        cost = 0
#    else:
#        cost = 1
#    
#    if result[t_len-1][s_len-1] != -1:
#        return result[t_len-1][s_len-1]
#    res = min([LevDist(s_peak, s_len - 1, t_peak, t_len    ) + 1,
#               LevDist(s_peak, s_len    , t_peak, t_len - 1) + 1, 
#               LevDist(s_peak, s_len - 1, t_peak, t_len - 1) + cost])
#    result[t_len-1][s_len-1] = res
#    return res

def LevDist2(s, t):
    slen = len(s)
    tlen = len(t)
    result = [[0 for i in range(len(s))] for j in range(len(t))]
    cost = 0

    for i in range(tlen):
        result[i][0] = i
    for j in range(slen):
        result[0][j] = j

    for i in range(tlen):
        for j in range(slen):
            if s[j-1] == t[i-1]:
                cost = 0
            else:
                cost = 1

            result[i][j] = min([result[i-1][j]+1,
                                result[i][j-1]+1,
                                result[i-1][j-1]+cost])
    return result[tlen-1][slen-1]

#if __name__ == '__main__':
#    
##    file = r'D:\Howard_Feng\NAO_Music_Autism_Project\Session1_6_7\record.wav'
##    file = r'D:\LabWork\ThesisProject\Music_Autism_Robot\Session1_6_7\record.wav'
#    file = r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Session1_6_7\record.wav'
#    sampleRate, data = wav.read(file)
#    N = len(data)
#    Nwin = 2048
#    xx = data[:, 0]
#    
#    low = 1040
#    high = 2800
#    x = bandpass_filter(xx, low, high, sampleRate, order=3)
#    # Generate a chirp: start frequency at 5 Hz and going down at 2 Hz/s
#    audioTime = np.arange(N) / sampleRate  # seconds
##    x = np.cos(2 * np.pi * time * (5 - 2 * 0.5 * time))
#
#    # Test with Nfft bigger than Nwin
#    Nfft = Nwin * 2
#    s = np.abs(stft(x, Nwin))
#    y = istft(s, Nwin)
#    peaks = findNotes(s, sampleRate/2)
#    realPeaks = realPeak(peaks)
#    start = time.time()
##    realPeaks = ['6', '7', '8', '9', '10', '9', '8', '6', '3', '6', '7', '8', '9', '8', '7', '6', '8', '7', '6', '5', '7']
#    r_len = len(realPeaks)
#    orgPeaks = ['6', '7', '8', '9', '10', '9', '8', '5', '3', '6', '7', '8', '9', '8', '7', '6', '8', '7', '6', '5', '7', '6']
#    o_len = len(orgPeaks)
#    result = [[-1 for i in range(len(realPeaks))] for j in range(len(orgPeaks))]
#    diff = LevDist2(realPeaks, orgPeaks)
##    diff = LevDist(realPeaks, r_len, orgPeaks, o_len)
#    end = time.time()
#    print("stft time: " + str(end - start))
#    print(diff)
    
    # Make sure the stft and istft are inverses. Caveat: `x` and `y` won't be
    # the same length if `N/Nwin` isn't integral!
#    maxerr = np.max(np.abs(x - y))
#    assert (maxerr < np.spacing(1) * 10)

#     Test `stftbins`
#    t, f = stftbins(x, Nwin, d=1.0 / sampleRate)
#    assert (len(t) == s.shape[0])
#    assert (len(f) == s.shape[1])
 
##    try:
#    import pylab as plt
#    plt.imshow(s, aspect="auto", extent=[f[0], f[-1], t[-1], t[0]])
#    plt.xlabel('frequency (Hertz)')
#    plt.ylabel('time (seconds (start of chunk))')
#    plt.title('STFT with chirp example')
#    plt.grid()
#    plt.show()
#    except ModuleNotFoundError:
#        pass