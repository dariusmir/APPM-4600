import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import scipy.linalg as scila
from time import time


def driver():

     ''' create  matrix for testing different ways of solving a square 
     linear system'''

     '''' N = size of system'''
     for N in [100, 500, 1000, 2000, 4000, 5000]:
      
          ''' Right hand side'''
          b = np.random.rand(N,1)
          A = np.random.rand(N,N)
          
          x = scila.solve(A,b)
          
          LU_factor_start = time()
          LU, P = scila.lu_factor(A)
          LU_factor_end = time()
          xlu = scila.lu_solve((LU, P), b)
          LU_end = time()


          test = np.matmul(A,x)
          r = la.norm(test-b)

          test_lu = np.matmul(A, xlu)
          r_lu = la.norm(test_lu - b)
          
          print('N = ', N)
          print('LU Factorization: ', LU_factor_end - LU_factor_start)
          print('LU Solve Process: ', LU_end - LU_factor_end)
          print('LU Total: ', LU_end - LU_factor_start)
          print('--')
          print('--')

     for N in range(1, 10):
          b = np.random.rand(N,1)
          A = np.random.rand(N,N)

          scila_time_start = time()
          x = scila.solve(A,b)
          
          LU_factor_start = time()
          LU, P = scila.lu_factor(A)
          LU_factor_end = time()
          xlu = scila.lu_solve((LU, P), b)
          LU_end = time()


          test = np.matmul(A,x)
          r = la.norm(test-b)

          test_lu = np.matmul(A, xlu)
          r_lu = la.norm(test_lu - b)

          if(LU_factor_start - scila_time_start > LU_end - LU_factor_start):
               print("For N: ", N)
               print('LU Total: ', LU_end - LU_factor_start)
               print('Normal Solver: ', LU_factor_start - scila_time_start)
               print('Number of N for normal is faster than scipy solver = ', N-1)
               break



     ''' Create an ill-conditioned rectangular matrix '''
     N = 10
     M = 5
     A = create_rect(N,M)     
     b = np.random.rand(N,1)


     
def create_rect(N,M):
     ''' this subroutine creates an ill-conditioned rectangular matrix'''
     a = np.linspace(1,10,M)
     d = 10**(-a)
     
     D2 = np.zeros((N,M))
     for j in range(0,M):
        D2[j,j] = d[j]
     
     '''' create matrices needed to manufacture the low rank matrix'''
     A = np.random.rand(N,N)
     Q1, R = la.qr(A)
     test = np.matmul(Q1,R)
     A =    np.random.rand(M,M)
     Q2,R = la.qr(A)
     test = np.matmul(Q2,R)
     
     B = np.matmul(Q1,D2)
     B = np.matmul(B,Q2)
     return B     
     
  
if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()       
