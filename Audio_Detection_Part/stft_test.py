import numpy as np
import numpy.fft as fft
from scipy.io import wavfile as wav
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt

def stft(x, Nwin, Nfft=None):

    """
    Short-time Fourier transform: convert a 1D vector to a 2D array
    The short-time Fourier transform (STFT) breaks a long vector into disjoint
    chunks (no overlap) and runs an FFT (Fast Fourier Transform) on each chunk.
    The resulting 2D array can 
    Parameters
    ----------
    x : array_like
        Input signal (expected to be real)
    Nwin : int
        Length of each window (chunk of the signal). Should be ≪ `len(x)`.
    Nfft : int, optional
        Zero-pad each chunk to this length before FFT. Should be ≥ `Nwin`,
        (usually with small prime factors, for fastest FFT). Default: `Nwin`.
    Returns
    -------
    out : complex ndarray
        `len(x) // Nwin` by `Nfft` complex array representing the STFT of `x`.
    
    See also
    --------
    istft : inverse function (convert a STFT array back to a data vector)
    stftbins : time and frequency bins corresponding to `out`
    """
    Nfft = Nfft or Nwin
    Nwindows = x.size // Nwin
    # reshape into array `Nwin` wide, and as tall as possible. This is
    # optimized for C-order (row-major) layouts.
    arr = np.reshape(x[:Nwindows * Nwin], (-1, Nwin))
    stft = fft.rfft(arr, Nfft)
    return stft


def stftbins(x, Nwin, Nfft=None, d=1.0):
    """
    Time and frequency bins corresponding to short-time Fourier transform.
    Call this with the same arguments as `stft`, plus one extra argument: `d`
    sample spacing, to get the time and frequency axes that the output of
    `stft` correspond to.
    Parameters
    ----------
    x : array_like
        same as `stft`
    Nwin : int
        same as `stft`
    Nfft : int, optional
        same as `stft`
    d : float, optional
        Sample spacing of `x` (or 1 / sample frequency), units of seconds.
        Default: 1.0.
    Returns
    -------
    t : ndarray
        Array of length `len(x) // Nwin`, in units of seconds, corresponding to
        the first dimension (height) of the output of `stft`.
    f : ndarray
        Array of length `Nfft`, in units of Hertz, corresponding to the second
        dimension (width) of the output of `stft`.
    """
    Nfft = Nfft or Nwin
    Nwindows = x.size // Nwin
    t = np.arange(Nwindows) * (Nwin * d)
    f = fft.rfftfreq(Nfft, d)
    return t, f


def istft(stftArr, Nwin):
    """
    Inverse short-time Fourier transform (ISTFT)
    Given an array representing the output of `stft`, convert it back to the
    original samples.
    Parameters
    ----------
    stftArr : ndarray
        Output of `stft` (or something the same size)
    Nwin : int
        Same input as `stft`: length of  each chunk that the STFT was calculated
        over.
    
    Returns
    -------
    y : ndarray
        Data samples corresponding to STFT data.
    
    See also:
    stft : the forward transform
    """
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
    notes = {'C6': 1038, 'D6': 1172, 'E6': 1316,
             'F6': 1389, 'G6': 1561, 'A6': 1755,
             'B6': 1975, 'C7': 2084, 'D7': 2343,
             'E7': 2626, 'F7': 2785}
    
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
            if rawPeak[i] >= note - 9 and rawPeak[i] <= note + 8:
                newPeak.append(key)
                print(newPeak)
                print(i)
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
            
    
    plt.plot(maxAmp)
    plt.show()
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
    
if __name__ == '__main__':
    
    file = r'D:\Howard_Feng\noteDetection\Audio_Detection_Part\promise.wav'
#    file = r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Audio_Detection_Part\promise.wav'
    sampleRate, data = wav.read(file)
    N = len(data)
    Nwin = 2048
    xx = data[:, 0]
    
    low = 1040
    high = 2800
    x = bandpass_filter(xx, low, high, sampleRate, order=3)
    # Generate a chirp: start frequency at 5 Hz and going down at 2 Hz/s
    time = np.arange(N) / sampleRate  # seconds
#    x = np.cos(2 * np.pi * time * (5 - 2 * 0.5 * time))

    # Test with Nfft bigger than Nwin
    Nfft = Nwin * 2
    s = np.abs(stft(x, Nwin))
    y = istft(s, Nwin)
    peaks = findNotes(s, sampleRate/2)
    realPeaks = realPeak(peaks)
    
    # Make sure the stft and istft are inverses. Caveat: `x` and `y` won't be
    # the same length if `N/Nwin` isn't integral!
#    maxerr = np.max(np.abs(x - y))
#    assert (maxerr < np.spacing(1) * 10)

    # Test `stftbins`
    t, f = stftbins(x, Nwin, d=1.0 / sampleRate)
    assert (len(t) == s.shape[0])
    assert (len(f) == s.shape[1])
 
    try:
#        import pylab as plt
        plt.imshow(s, aspect="auto", extent=[f[0], f[-1], t[-1], t[0]])
        plt.xlabel('frequency (Hertz)')
        plt.ylabel('time (seconds (start of chunk))')
        plt.title('STFT with chirp example')
        plt.grid()
        plt.show()
    except ModuleNotFoundError:
        pass