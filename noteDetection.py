import numpy as np
import matplotlib.pyplot as plt
import wave
import scipy.fftpack
from scipy import io
import soundfile as sf

fileName1 = r'C:\Users\fengh\pythonProject\noteDetection\guitar1.wav'  # get the file name from the hard drive
fileName2 = r'C:\Users\fengh\pythonProject\noteDetection\guitar2.wav'  # get the file name from the hard drive

waveData1, Fs1 = sf.read(fileName1)
waveData2, Fs2 = sf.read(fileName2)

#fftData = np.fft.fft(np.transpose(A)) # np.fft.fft only takes row vector
#print(fftData)


waveFile1 = wave.open(fileName1, 'rb')   # open the file, 'rb' for read the file to python
# sampFreq, snd = wavefile.read('guitar1.wav')

# the music file used in this program recorded by Howard
# frequence rate 44.1kHz, 16 bit, one channel 7 seconds

params1 = waveFile1.getparams()  # getting basic info from the audio file
nchannels1, sampwidth1, framerate1, nframes1 = params1[:4]
L1 = nframes1 / framerate1 * 1000 # for getting all float number, I multiplied 1.0 to change the number
# and the length of the file is L and we use it as millisecond
Fs1 = framerate1  # sampling rate
N1 = nframes1     # total samples
C1 = nchannels1   # channel numbers
Ts1 = 1.0 / Fs1   # timestep
t1 = scipy.arange(0.0, L1/1000, Ts1)    # time vector
sampleNumber1 = len(t1)

waveData1 = waveData1[range(0, sampleNumber1)]


print("channel numbers = \n", C1)
print("sample width = \n", sampwidth1)
print("sampling frequence = \n", Fs1)
print("total frames = \n", N1)
print("total length = \n", L1)

#waveData1 = waveData[range(0, L, 1)]
print("This is the original wave data\n", waveData1)
# fftData = scipy.fft(waveData)
fftData1 = abs(np.fft.rfft(waveData1)/L1)
print("This is the transformed data after fft\n", fftData1)
fftDataHalf1 = fftData1[range(1, L1/2+1, 1)]
frequencyData1 = 2 * fftDataHalf1[range(0, L1/2, 1)]

#freqs = scipy.fftpack.fftfreq(waveData.size, t[1]-t[0])
#fftFreqs = np.array(freqs)
#freqsHalf = freqs[range(N/2)]
f1 = np.array(range(0, L1/2, 1)) * Fs1 / L1


plt.figure(1)
plt.subplot(2,1,1)
plt.plot(t1, waveData1, "g")
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(2,1,2)
plt.plot(f1/32, frequencyData1, "r")
plt.xlabel('Frequency(Hz)')
plt.ylabel('Count single-sided')
plt.show()
'''
waveFile2 = wave.open(fileName2, 'rb')   # open the file, 'rb' for read the file to python
# sampFreq, snd = wavefile.read('guitar1.wav')

# the music file used in this program recorded by Howard
# frequence rate 44.1kHz, 16 bit, one channel 7 seconds

params2 = waveFile2.getparams()  # getting basic info from the audio file
nchannels2, sampwidth2, framerate2, nframes2 = params2[:4]
L2 = nframes2 / framerate2 * 1000 # for getting all float number, I multiplied 1.0 to change the number
# and the length of the file is L and we use it as millisecond
Fs2 = framerate2  # sampling rate
N2 = nframes2     # total samples
C2 = nchannels2   # channel numbers
Ts2 = 1.0 / Fs2   # timestep
t2 = scipy.arange(0.0, L2/1000, Ts2)    # time vector
sampleNumber2 = len(t2)

waveData2 = waveData2[range(0, sampleNumber2)]


print("channel numbers = \n", C2)
print("sample width = \n", sampwidth2)
print("sampling frequence = \n", Fs2)
print("total frames = \n", N2)
print("total length = \n", L2)

#waveData1 = waveData[range(0, L, 1)]
print("This is the original wave data\n", waveData2)
# fftData = scipy.fft(waveData)
fftData2 = abs(np.fft.rfft(waveData2)/L2)
print("This is the transformed data after fft\n", fftData2)
fftDataHalf2 = fftData2[range(1, L2/2+1, 1)]
frequencyData2 = 2 * fftDataHalf2[range(0, L2/2, 1)]

#freqs = scipy.fftpack.fftfreq(waveData.size, t[1]-t[0])
#fftFreqs = np.array(freqs)
#freqsHalf = freqs[range(N/2)]
f2 = np.array(range(0, L2/2, 1)) * Fs2 / L2


plt.figure(2)
plt.subplot(2,1,1)
plt.plot(t2, waveData2, "g")
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(2,1,2)
plt.plot(f2/32, frequencyData2, "r")
plt.xlabel('Frequency(Hz)')
plt.ylabel('Count single-sided')
plt.show()

'''