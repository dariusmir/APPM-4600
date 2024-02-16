import matplotlib.pyplot as plt
import numpy as np
import math
import scipy
from bisection import bisection
from fixedpt import fixedpt

def P1():
	f=  lambda x: 2*x-1-np.sin(x)

	tol = 1e-8
	a = 0
	b = 1
	Nmax = 100

	[astar, ier, count] = bisection(f, a, b, tol, Nmax)
	print('The approximate root is: ',astar)
	print('The number of iterations is: ', count)

#P1()

def P2():
	f = lambda x: (x-5)**9

	tol = 1e-4
	a = 4.82
	b = 5.2
	NMax = 100

	[astar, ier, count] = bisection(f, a, b, tol, NMax)
	print('The approximate root is: ',astar)
	print('The number of iterations is: ', count)


	f = lambda x: -1953125 + 3515625*x - 2812500*x**2 + 1312500*x**3 - 393750*x**4 - 78750*x**5 - 10500*x**6 + 900*x**7 - 45*x**8 + x**9
	[astar, oer, count] = bisection(f, a, b, tol, NMax)
	print('The approximate root is: ',astar)
	print('The number of iterations is: ', count)

#P2()

def P3():
	f = lambda x: x**3+x-4
	tol = 1e-3
	a = 1
	b = 4
	NMax = 100

	[astar, oer, count] = bisection(f, a, b, tol, NMax)
	print('The approximate root is: ',astar)
	print('The number of iterations is: ', count)

#P3()

def P5():
	f = lambda x: x-5*np.sin(2*x)-3
	x= np.linspace(-5, 10, 100)
	tol = 1e-10
	Nmax = 100
	x0 = 3

	[xstar, ier] = fixedpt(f, x0, tol, Nmax)

	plt.figure()
	plt.savefig('5a')
	plt.plot(x, f(x))
	plt.plot(x, np.linspace(0, 0, 100))
	plt.grid()
	plt.show()
	

	f = lambda x: -np.sin(2*x)+5*x/4-3/4
	g = lambda x: 5/4-2*np.cos(2*x)


	plt.figure()
	plt.savefig('5b')
	plt.plot(x, f(x))
	plt.plot(x, g(x))
	plt.plot(x, np.linspace(0, 0, 100))
	plt.legend(['f(x)', 'g(x)'])
	plt.grid()
	plt.show()
	
	

P5()



















