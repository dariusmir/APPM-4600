# import libraries
import numpy as np

# define routines
def fixedpt(f,x0,tol,Nmax):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    i = 0
    xArr = np.zeros(Nmax)

    while (count < Nmax):
       count = count +1
       x1 = f(x0)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          xArr[i] = xstar
          return [xArr,ier, count]
          i += 1
       x0 = x1
       xArr[i] = x0
       i += 1

    xstar = x1
    xArr[i] = xstar
    ier = 1
    return [xArr, ier, count]
    i += 1