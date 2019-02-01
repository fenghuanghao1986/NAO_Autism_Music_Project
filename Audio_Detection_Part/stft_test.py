import numpy as np
<<<<<<< HEAD
import scipy.io.wavfile as wavfile
from scipy.interpolate import interp1d
from scipy.signal import argrelextrema
#def stft(x, Nwin, Nfft=None):
#    """
#    Short-time Fourier transform: convert a 1D vector to a 2D array
#    The short-time Fourier transform (STFT) breaks a long vector into disjoint
#    chunks (no overlap) and runs an FFT (Fast Fourier Transform) on each chunk.
#    The resulting 2D array can 
#    Parameters
#    ----------
#    x : array_like
#        Input signal (expected to be real)
#    Nwin : int
#        Length of each window (chunk of the signal). Should be ≪ `len(x)`.
#    Nfft : int, optional
#        Zero-pad each chunk to this length before FFT. Should be ≥ `Nwin`,
#        (usually with small prime factors, for fastest FFT). Default: `Nwin`.
#    Returns
#    -------
#    out : complex ndarray
#        `len(x) // Nwin` by `Nfft` complex array representing the STFT of `x`.
#    
#    See also
#    --------
#    istft : inverse function (convert a STFT array back to a data vector)
#    stftbins : time and frequency bins corresponding to `out`
#    """
#    Nfft = Nfft or Nwin
#    Nwindows = x.size // Nwin
#    # reshape into array `Nwin` wide, and as tall as possible. This is
#    # optimized for C-order (row-major) layouts.
#    arr = np.reshape(x[:Nwindows * Nwin], (-1, Nwin))
#    stft = np.fft.rfft(arr, Nfft)
#    return stft
##
file = r'C:\Users\fengh\pythonProject\NAO_Autism_Music_Project\Audio_Detection_Part\new_xylo\ace.wav'
##
waveData, fs = sf.read(file)
##
#lowcut = 1000.0
#highcut = 3000.0
##
#y = butter_bandpass_filter(waveData, lowcut, highcut, fs, order=3)
##
#
#zxx = stft(y[:,0], 10)
#
#t = len(waveData)/fs
#
#
#
##
#
##fs = 10e3
##N = 1e5
##amp = 2 * np.sqrt(2)
###noise_power = 0.01 * fs / 2
##time = np.arange(N) / float(fs)
##mod = 500*np.cos(2*np.pi*0.25*time)
##carrier = np.sin(2*np.pi*3e3*time + mod)
##
##f, t, Zxx = signal.stft(carrier, fs, nperseg=1000)
## =============================================================================
#plt.plot(zxx)
## =============================================================================
#plt.show()
##plt.pcolormesh(t, f, np.abs(Zxx), vmin=0, vmax=amp)
##plt.title('STFT Magnitude')
##plt.ylabel('Frequency [Hz]')
##plt.xlabel('Time [sec]')
##plt.show()
=======
import numpy.fft as fft
from scipy.io import wavfile as wav
from scipy.signal import butter, lfilter

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
>>>>>>> ea0db5a020f3280e475d3112e0bcee4d9c489aec


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

def findNotes(stftData):
    x = len(stftData)
    maxAmp = []
    maxLocal = []
    for i in range(x):
        maxAmp.append(stftData[i].max())
    
    plt.plot(maxAmp)
    plt.show()
    for i in range(x):
        if (i == 0):
            if (maxAmp[i] >= maxAmp[i+1]):
                maxLocal.append(maxAmp[i])
        elif (i == x-1):
            if (maxAmp[i] >= maxAmp[i-1]):
                maxLocal.append(maxAmp[i])
        elif (maxAmp[i] >= maxAmp[i-1]) and (maxAmp[i] >= maxAmp[i+1]):
            maxLocal.append(maxAmp[i])
#            
    return maxLocal
    
if __name__ == '__main__':
    
    file = r'D:\Howard_Feng\noteDetection\Audio_Detection_Part\promise.wav'
    sampleRate, data = wav.read(file)
    N = len(data)
    Nwin = 1024
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
    peaks = findNotes(s)
    # Make sure the stft and istft are inverses. Caveat: `x` and `y` won't be
    # the same length if `N/Nwin` isn't integral!
#    maxerr = np.max(np.abs(x - y))
#    assert (maxerr < np.spacing(1) * 10)

    # Test `stftbins`
    t, f = stftbins(x, Nwin, d=1.0 / sampleRate)
    assert (len(t) == s.shape[0])
    assert (len(f) == s.shape[1])
 
#    try:
#        import pylab as plt
#        plt.imshow(s, aspect="auto", extent=[f[0], f[-1], t[-1], t[0]])
#        plt.xlabel('frequency (Hertz)')
#        plt.ylabel('time (seconds (start of chunk))')
#        plt.title('STFT with chirp example')
#        plt.grid()
#        plt.show()
#    except ModuleNotFoundError:
#        pass