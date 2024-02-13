import numpy as np

#[1. 1.42073549 1.49438099 1.49854088 1.49869536 1.49870093 1.49870113]

def Aitken(seq, tol, NMax):
	pHat = np.zeros(NMax)
	i = 0
	while i < len(seq[:-2]):
		i += 1

		pHat[i] = np.array(seq[i] - ((seq[i+1] - seq[i])**2) / (seq[i+2] - 2*seq[i+1] + seq[i]))
		if(np.abs(pHat[i]-seq[-1]) < tol):
			#pHat[i] = pHat
			return [np.trim_zeros(pHat), i]
	return [np.trim_zeros(pHat), i]




