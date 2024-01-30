import numpy as np
import numpy.linalg as la
import math

#Matrix Multiplication Test
def driver():
	A  = np.matrix([[3, 4], [5, 6]])

	B = np.matrix([[7, 8], [9, 10]])

	row = len(A)
	x = np.empty([row, row])
	for i in range(row):
		for j in range(row):
			temp = dotProduct(A[i, :], B[:, j].T, row)
			x[i, j] = temp

	print(x)
	return

def dotProduct(x,y,n):
	dp = 0.
	for j in range(n):
		dp = dp + x[0, j]*y[0, j]

	return dp  

driver()