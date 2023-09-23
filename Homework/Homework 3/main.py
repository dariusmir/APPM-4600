import numpy as np
from matplotlib import pyplot as plt
from fixedpt import fixedpt

t = np.linspace(-5,5,10000)
f = lambda x: x - 4*np.sin(2*x)-3

#plt.plot(t, f(t))
#plt.grid()
#plt.show()

tol = 1e-8
Nmax = 1000

f = lambda x: -np.sin(2*x) + (5*x)/4 - 3/4

plt.plot(t, f(t))
plt.grid()
plt.show()

x0 = 5
[xstar,ier] = fixedpt(f,x0,tol,Nmax)
print('the approximate fixed point is:',xstar)
print('f1(xstar):',f(xstar))
print('Error message reads:',ier)



