# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 09:00:12 2019

@author: fengh
"""

from scipy.io.wavfile import read, write
from scipy.signal.filter_design import butter, buttord
from scipy.signal import lfilter
from numpy import asarray
def convert_hertz(freq):
    # convert frequency in hz to units of pi rad/sample
    # (our .WAV is sampled at 44.1KHz)
    return freq * 2.0 / 44100.0

rate, sound_samples = read('9.wav')
pass_freq = convert_hertz(440.0) # pass up to 'middle C'
stop_freq = convert_hertz(440.0 * 4) # max attenuation from 3 octaves
pass_gain = 3.0 # tolerable loss in passband (dB)
stop_gain = 60.0 # required attenuation in stopband (dB)
ord, wn = buttord(pass_freq, stop_freq, pass_gain, stop_gain)
b, a = butter(ord, wn, btype = 'low')
filtered = lfilter(b, a, sound_samples)
integerised_filtered = asarray(filtered, int)
write('0.wav', rate, integerised_filtered)