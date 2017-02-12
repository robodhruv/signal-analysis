from cmath import exp, pi
from math import ceil, log, modf
import numpy as np

def extend_domain(sound, N):
	n = N - 1
	if not (modf(log(n, 2))[0] == 0.0):
		sound.extend([0] * int(2**(ceil(log(n, 2))) - len(sound)))


def fft_i(sequence):
	# Cooley - Tuckey Algorithm
	seq = list(sequence)
	N = len(seq)
	threshold = 16
	if N <= threshold:
		return vectorized_fft(seq)
	even = fft_i(seq[0::2])
	odd =  fft_i(seq[1::2])

	if (len(odd) < N//2 - 1):
		print "Error"
	T= [exp(-2j*pi*k/N)*odd[k] for k in range(N//2)]
	return [even[k] + T[k] for k in range(N//2)] + \
			[even[k] - T[k] for k in range(N//2)]

def ifft_i(sequence):
	# Cooley - Tuckey Algorithm Extended
	seq = list(sequence)
	N = len(seq)
	threshold = 32
	if N <= threshold:
		return vectorized_ifft(seq)
	even = ifft_i(seq[0::2])
	odd =  ifft_i(seq[1::2])
	if (len(odd) < N//2 - 1): print "Error"
	T= [exp(2j*pi*k/N)*odd[k] for k in range(N//2)]
	return [even[k] + T[k] for k in range(N//2)] + \
			[even[k] - T[k] for k in range(N//2)]

def vectorized_fft(x):
	# At a unit level, we compute the vectorised ifft
	x = np.asarray(x, dtype=np.cfloat)
	N = x.shape[0]
	n = np.arange(N)
	k = n.reshape((N, 1))
	M = np.exp(-2j * np.pi * k * n / N)
	return list(np.dot(M, x))

def vectorized_ifft(x):
	# At a unit level, we compute the vectorised ifft
	x = np.asarray(x, dtype=np.cfloat)
	N = x.shape[0]
	n = np.arange(N)
	k = n.reshape((N, 1))
	M = np.exp(2j * np.pi * k * n / N)
	return list(np.dot(M, x))


def iFFT(x):
	x = np.asarray(x, dtype=np.cfloat)
	N = x.shape[0]
	if N <= 32:  # this cutoff should be optimized
		return vectorized_ifft(x)
	else:
		X_even = iFFT(x[::2])
		X_odd = iFFT(x[1::2])
		factor = np.exp(2j * np.pi * np.arange(N) / N)
		return np.concatenate([X_even + factor[:N / 2] * X_odd, X_even + factor[N / 2:] * X_odd])





def FFT_vectorized(x):
	"""A vectorized, non-recursive version of the Cooley-Tukey FFT"""
	x = np.asarray(x, dtype=np.cfloat)
	N = x.shape[0]

	if np.log2(N) % 1 > 0:
		raise ValueError("size of x must be a power of 2")

	# N_min here is equivalent to the stopping condition above,
	# and should be a power of 2
	N_min = min(N, 32)
	
	# Perform an O[N^2] DFT on all length-N_min sub-problems at once
	n = np.arange(N_min)
	k = n[:, None]
	M = np.exp(-2j * np.pi * n * k / N_min)
	X = np.dot(M, x.reshape((N_min, -1)))

	# build-up each level of the recursive calculation all at once
	while X.shape[0] < N:
		X_even = X[:, :X.shape[1] / 2]
		X_odd = X[:, X.shape[1] / 2:]
		factor = np.exp(-1j * np.pi * np.arange(X.shape[0])
						/ X.shape[0])[:, None]
		X = np.vstack([X_even + factor * X_odd,
					   X_even - factor * X_odd])

	return X.ravel()

def iFFT_vectorized(x):
	"""A vectorized, non-recursive version of the Cooley-Tukey FFT"""
	x = np.asarray(x, dtype=np.cfloat)
	N = x.shape[0]

	if np.log2(N) % 1 > 0:
		raise ValueError("size of x must be a power of 2")

	# N_min here is equivalent to the stopping condition above,
	# and should be a power of 2
	N_min = min(N, 32)
	
	# Perform an O[N^2] DFT on all length-N_min sub-problems at once
	n = np.arange(N_min)
	k = n[:, None]
	M = np.exp(2j * np.pi * n * k / N_min)
	X = np.dot(M, x.reshape((N_min, -1)))

	# build-up each level of the recursive calculation all at once
	while X.shape[0] < N:
		X_even = X[:, :X.shape[1] / 2]
		X_odd = X[:, X.shape[1] / 2:]
		factor = np.exp(-1j * np.pi * np.arange(X.shape[0])
						/ X.shape[0])[:, None]
		X = np.vstack([X_even + factor * X_odd,
					   X_even - factor * X_odd])

	return X.ravel()