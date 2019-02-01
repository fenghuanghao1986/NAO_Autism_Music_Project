# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 18:50:01 2019

@author: CV_LAB_Howard
"""

# a test code for stft

from scipy import signal
import matplotlib.pyplot as plt
import soundfile as sf
from bandpass_fft_series_getPeaks import butter_bandpass_filter 
import numpy as np
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

rate, data = wavfile.read(waveData)
time = np.arange(len(data[:,0]))*1.0/rate

#plt.plot(time,data[:,0])
#plt.show()

nfft = 1024*6
pxx, freq, bins, plot = plt.specgram(data[:,0],NFFT=nfft)

plt.show()

a = np.mean(pxx,axis=0)
aa = np.arange(len(a))
a = a/np.max(a)*np.max(data[:,0])
aa = aa/np.max(aa) * time[-1]

f = interp1d(aa,a)
newSmooth = f(time)

indMax = argrelextrema(newSmooth, np.greater)[0]
indMin = argrelextrema(newSmooth, np.less)[0]

lastValue = np.where(newSmooth==newSmooth[-1])[0]
indMin = np.hstack((indMin,lastValue))

plt.plot(time,data[:,0])
plt.plot(aa,a)
plt.plot(time[indMax],newSmooth[indMax])
plt.plot(time[indMin],newSmooth[indMin])
plt.show()