import numpy as np
import numpy.linalg as la
import math

def driver():
	A  = np.matrix([[3, 4], [5, 6], [7, 8]]) #Initialize Matrix A

	B = np.matrix([[3, 4, 5], [5, 6, 7]]) #Initialize Matrix B

	#Extract the rows and columns of matrix A and B
	rowA = A.shape[0]
	colA = A.shape[1]
	rowB = B.shape[0]
	colB = B.shape[1]

	#Checking if matrix multiplication is valid or not
	if colA != rowB:
		print('Matrices are not valid')
	else:
		x = np.empty([colA, rowB]) #Creates an empty matrix, with the rows and columns of the new matrix
		for i in range(colA):
			for j in range(rowB):
				temp = dotProduct(A[i, :], B[:, j].T, rowB) #Takes the dot product of the row of matrix A, with the column of matrix B
				x[i, j] = temp

		print(x)
	return

#Function for finding the dot product
def dotProduct(x,y,n):
	dp = 0.
	for j in range(n):
		dp = dp + x[0, j]*y[0, j]

	return dp  

driver()