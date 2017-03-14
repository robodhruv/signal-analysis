import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

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