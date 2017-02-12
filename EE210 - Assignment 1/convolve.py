from fft_pkg import *
import matplotlib.pyplot as plt
from scipy.io import wavfile

dir = "Files/"
results_dir = dir + "results/"
FIR = "parking_garage_16k"
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

		X = np.asarray(fft_i(input_sound))
		IR_l = np.asarray(fft_i(IR_L))
		IR_r = np.asarray(fft_i(IR_R))

		Y1 = X * IR_l
		y1 = ifft_i(Y1)

		Y2 = X * IR_r
		y2 = ifft_i(Y2)

		yr1 = np.real(y1)
		yr1 /= max(yr1) * 1.01
		yr1 = yr1[:N]

		yr2 = np.real(y2)
		yr2 /= max(yr2) * 1.01
		yr2 = yr2[:N]

		yr = np.empty([np.shape(yr1)[0], 2])
		yr[:,0] = yr1
		yr[:,1] = yr2
		print np.shape(yr)

		wavfile.write(results_dir + FIR + "_complete.wav", sampling_sound, yr)