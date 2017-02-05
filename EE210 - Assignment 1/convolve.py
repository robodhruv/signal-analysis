from fft import *
import matplotlib.pyplot as plt
from scipy.io import wavfile

dir = "Files/"
results_dir = dir + "results/"
FIR = "Five_Columns_Long_16k"
Source_Sound = "BheegiRegular"

if __name__ == '__main__':
	sampling_IR, IR = wavfile.read(dir + FIR + ".wav")
	sampling_sound, input_sound = wavfile.read(dir + Source_Sound + ".wav")
	if (sampling_sound == sampling_IR):
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

		wavfile.write(results_dir + FIR + "_complete.wav", sampling_sound, yr)