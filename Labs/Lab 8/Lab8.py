import matplotlib.pyplot as plt
import numpy as np
import math
from line import find_points
from line import eval_line


def driver():
    
  f = lambda x: 1/(1+(10*x)**2)
  a = -1
  b = 1
  
  ''' create points you want to evaluate at'''
  Neval = 100
  xeval =  np.linspace(a,b,Neval)
  
  ''' number of intervals'''
  Nint = 10
  
  '''evaluate the linear spline'''
  yeval = eval_lin_spline(xeval,Neval,a,b,f,Nint)
  
  ''' evaluate f at the evaluation points'''
  fex = np.zeros(Neval)
  for j in range(Neval):
    fex[j] = f(xeval[j]) 

  plt.figure()
  plt.plot(xeval,fex,'r-')
  plt.plot(xeval,yeval,'b-')
  plt.show()
   
  err = abs(yeval-fex)
  plt.figure()
  plt.title('Error')
  plt.plot(xeval,err,'r-')
  plt.show()

    
    
def eval_lin_spline(xeval,Neval,a,b,f,Nint):

  xint = np.linspace(a,b,Nint+1)
  xeval = np.linspace(a,b, Neval)

  yeval = np.zeros(Neval)
  
  for jint in range(Nint):

    ind = find_points(xeval, xint, jint)

    a1= xint[jint]
    fa1 = f(a1)
    b1 = xint[jint+1]
    fb1 = f(b1)
    
    for kk in ind:
        '''use your line evaluator to evaluate the lines at each of the points 
        in the interval'''
        '''yeval(ind(kk)) = call your line evaluator at xeval(ind(kk)) with 
        the points (a1,fa1) and (b1,fb1)'''
        yeval[kk] = eval_line(a1, fa1, b1, fb1, xeval[kk])
  
  return yeval

           
if __name__ == '__main__':
      # run the drivers only if this is called from the command line
      driver()               