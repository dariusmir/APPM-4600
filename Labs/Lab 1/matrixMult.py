import numpy as np
import numpy.linalg as la
import math

def driver():
	A  = np.matrix([[3, 4], [5, 6], [7, 8]])

	B = np.matrix([[3, 4, 5], [5, 6, 7]])

	rowA = A.shape[0]
	colA = A.shape[1]
	rowB = B.shape[0]
	colB = B.shape[1]

	if colA != rowB:
		print('Matrices are not valid')
	else:
		x = np.empty([colA, rowB])
		for i in range(colA):
			for j in range(rowB):
				temp = dotProduct(A[i, :], B[:, j].T, rowB)
				x[i, j] = temp

		print(x)
	return

def dotProduct(x,y,n):
	dp = 0.
	for j in range(n):
		dp = dp + x[0, j]*y[0, j]

	return dp  

driver()