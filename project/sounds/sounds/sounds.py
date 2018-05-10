#!/usr/bin/env/python

"a package for visualizing a .wav file as a spectrogram, waveform, and periodogram"

import pickle
import numpy as np
import matplotlib.pyplot as plt
import os
import wave
import pylab
from scipy import signal


class Sounds:
    """
    Create a Sounds class instance with a spectrogram, waveform, and periodogram 
    saved as arrays
    """
    def __init__(self, wav):
        self.wav = wav


    def _graph_spectrogram(self):
        """
        Returns and saves a spectrogram image visualizing the .wav file as 
        frequency over time, depicting amplitude with color.
        """
        sound_info, frame_rate = get_wav_info(self.wav)
        pylab.figure(num=None, figsize=(19, 12))
        pylab.subplot(111)
        pylab.title('spectrogram of %r' % self.wav)
        pylab.specgram(sound_info, Fs=frame_rate)
        pylab.savefig('spectrogram.png')

    def _get_wav_info(self):
        "Returns sound_info and frame_rate as an array"
        wav = wave.open(self.wav, 'r')
        frames = wav.readframes(-1)
        sound_info = pylab.fromstring(frames, 'int16')
        frame_rate = wav.getframerate()
        wav.close()
        return sound_info, frame_rate

    def save_spec(self):
        """
        Displays and saves spectrogram using _graph_spectrogram() and
        _get_wav_info(), saving the spectrogram as an array using pickles.
        """
        _graph_spectrogram(self)
        _get_wav_info(self)
        pickle.dump([times, frequencies, spectrogram], open('data.pickle', 'wb'))
        # this saves the image as an array for use with the rest of the code

    def get_waveform(self):
        "Displays waveform using data saved with pickles"
        # open the data
        data = pickle.load(open('/Users/juliazeh/PDSB/PDSB-project/data_raw.pickle'))
        sample_rate = data[0]
        samples = data[1]
        # find time axis
        seconds = len(samples)/sample_rate
        time_axis = np.linspace(0, seconds, len(samples))
        print len(time_axis)
        # plot waveform
        from IPython import get_ipython
        get_ipython().run_line_magic('matplotlib', 'inline')
        plt.plot(time_axis, samples)
        plt.ylabel('amplitude (dBFS)')
        plt.xlabel('time (seconds)')

    def get_periodogram(self):
        "Displays periodogram using data saved with pickles"
        # open the data
        data = pickle.load(open('/Users/juliazeh/PDSB/PDSB-project/data_raw.pickle'))
        samples = data[1]
        f, p = signal.periodogram(samples)
        plt.semilogx(f, p)
        plt.ylabel('power')
        plt.xlabel('frequency (kHz)')
