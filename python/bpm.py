from numpy import *
import scipy.io.wavfile as wio
from scipy import signal as sig
from scipy import misc

import matplotlib.pyplot as plt
import numpy.linalg as la

# takes frames
# returns a 2D similarity matrix and the duration of the sample
def simMatrix(frames):
	rows = len(frames)

	sim = zeros((rows, rows))
	for i in xrange(0, rows):
		for j in xrange(0, rows):
			fi = frames[i]
			fj = frames[j]
			mag = (la.norm(fi)*la.norm(fj))

			if mag == 0.:
				sim[i][j] = 1
			else:
				sim[i][j] = dot(fi, fj)/(la.norm(fi)*la.norm(fj))

	# plt.matshow(sim, cmap='bone', origin='lower')

	# plt.xlabel('i')
	# plt.ylabel('j')
	# plt.title('Music Similarity Matrix')

	# plt.show()

	return sim

# Finds beat spectrum with length dur for a given similarity matrix with a given duration
# along a time interval T with start time t0
def beatSpectrum(smat, dur, T, t0, rate):
	X = len(smat)
	samples = int(X*float(T)/dur)

	offset = int(X*float(t0)/dur)

	spec = zeros(samples)
	for i in xrange(0, samples):
		sum = 0
		for j in xrange(0, samples):
			sum += smat[offset+i + j, j]
		spec[i] = sum

	plt.plot(linspace(0, T, len(spec)), spec)

	plt.xlabel('Time (seconds)')
	plt.ylabel('Beat Spectrum')

	plt.title('Beat Spectrum Intensity Over Time')

	plt.show()
	return spec

def autocorr(x):
    corr2d = sig.correlate2d(x, x, mode='same')

    corr = [std(c) for c in corr2d]

    return corr








