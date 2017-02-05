from fft import *
import matplotlib.pyplot as plt
from scipy.io import wavfile

dir = "Files/"
FIR = "long_echo_hall_16k.wav"
Source_Sound = "BheegiRegular-part.wav"

if __name__ == '__main__':
	sampling_IR, IR = wavfile.read(dir + FIR)
	sampling_sound, input_sound = wavfile.read(dir + Source_Sound)

	IR_L = IR[:, 0]
	IR_R = IR[:, 1]

	N = len(IR_L) + len(input_sound)

	input_sound = list(input_sound)
	IR_L = list(IR_L)
	IR_R = list(IR_R)

	extend_domain(input_sound, N)
	extend_domain(IR_L, N)
	extend_domain(IR_R, N)

	X = np.asarray(fft(input_sound))
	IR = np.asarray(fft(IR_L))

	Y = X * IR
	y = ifft(Y)

	yr = np.real(y)
	yr /= max(yr) * 1.01

	wavfile.write('out1.wav', sampling_sound, yr)

