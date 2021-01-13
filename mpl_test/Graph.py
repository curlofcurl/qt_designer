#!/usr/bin/env python3

from scipy.fft import fft
from scipy.io import wavfile
import scipy.signal as signal
import numpy as np
import soundfile as sf

class Graph:
    def __init__(self):
        pass


class Mathpro:
    def __init__(self):
        self.files = []

    def setFile(self, filename):
        self.files.append(filename)

    def runfft(self, file):
        ob = sf.Soundfile(file)
        fs, data = wavfile.read(file)
        a = data.T
        a = signal.detrend(a)
        b = a
        c = fft(b)
        d = len(c/2)
        x = np.linsapce(0, ob.samplerate/2, ob.frames-1)
        realfft = abs(c[:int(d-1)])

        return np.array([x, realfft])

    def getSpectro(self, file):
        fs, data = wavfile.read(file)
        f, t, Sxx = signal.spectrogram(data, fs, nfft=1024)

        return f, t, Sxx

