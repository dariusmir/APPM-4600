import numpy as np
from fixedpt import fixedpt
from Aitken import Aitken
	
#f = lambda x: 1+0.5*np.sin(x)
f = lambda x: (10 / (x+4))**0.5
x0 = 0.0
tol = 1e-6
Nmax = 1000
[xArr, ier, count] = fixedpt(f,x0,tol,Nmax)
xArr = xArr[xArr != 0]
print('Prelab')
print('the fixed point iteration array is:', xArr)
print('the approximate fixed point is:',xArr[-1])
print('the number of iterations is:',count)
#print('f2(xstar):',f(xstar))
print('Error message reads:',ier)



[pHat, count] = Aitken(xArr, tol, Nmax)
print('\nQ3.2')
print('the Aitken array is:', pHat)
print('the approximate fixed point is:',xArr[-1])
print('the number of iterations is:', count)

