import matplotlib.pyplot as plt
import numpy as np

Fs = 150.0  # sampling rate
Ts = 1.0/Fs # sampling interval
t = np.arange(0., 1., Ts) # time vector

ff = 5   # frequency of the signal
y = np.sin(2*np.pi*ff*t)  # sample signal
n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
frq = frq[range(n/2)] # one side frequency range

Y = np.fft.fft(y)/n # fft computing and normalization
Y = np.absolute(Y[range(n/2)])

plt.plot(Y)
plt.show()

