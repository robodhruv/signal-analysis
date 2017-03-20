import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import csv
import re


def get_sinusoid(a, f, phi, duration):
	"""
	Takes input the following quatities:
	Amplitude (a) a number between 0 and 1.
	Frequency (f) in Hertz.
	Phase (phi) in radians. You may use np.pi for convenience.
	Duration in milliseconds.
	"""

	sampling_rate = 16000
	t = np.arange(0, duration/1000., 1./sampling_rate)
	x = a * np.sin((2 * np.pi * f * t) + phi)
	return x

def get_notes(songfile):
	song = []
	with open(songfile, 'rb') as csvfile:
		songreader = csv.reader(csvfile, delimiter = ' ')
		for row in songreader:
			song.append(row)
	return song

def strip_file(songfile):
	stripped = []
	with open(songfile, 'rb') as song_file:
		for row in song_file:
			stripped.append(re.sub(r';', "", re.sub(
				r'\)', "", re.sub(r'\(', "", row))))
	song_file.close()
	with open(songfile, 'wb') as new_file:
		for el in stripped:
			new_file.write(el)

get_notes("Songs/song_b.txt")