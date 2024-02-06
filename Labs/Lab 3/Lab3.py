import matplotlib.pyplot as plt
import numpy as np
import math
from bisection import bisection
from fixedpt import fixedpt


def Problem1():
	# use routines
	f = lambda x: x**2*(x-1)
	a = 0.5
	b = 2
	tol = 1e-7
	Nmax = 1000

	print('\nfor a = 0.5 and b = 2')
	[astar,ier] = bisection(f,a,b,tol, Nmax)
	print('the approximate root is',astar)
	print('the error message reads:',ier)
	print('\nf(astar) =', f(astar))

	a = -1
	b = 0.5
	print('\nfor a = -1 and b = 0.5')
	[astar,ier] = bisection(f,a,b,tol, Nmax)
	print('the approximate root is',astar)
	print('the error message reads:',ier)
	print('\nf(astar) =', f(astar))

	a = -1
	b = 2
	print('\nfor a = -1 and b = 2')
	[astar,ier] = bisection(f,a,b,tol, Nmax)
	print('the approximate root is',astar)
	print('the error message reads:',ier)
	print('\nf(astar) =', f(astar))


#Problem1()


def Problem2():
	print("\nProblem 2")
	print("\n")

	a = 0
	b = 2.4
	tol = 1e-5
	Nmax = 1000
	p1 = lambda x: (x-1)*(x-3)*(x-5)
	[astar,ier] = bisection(p1,a,b,tol, Nmax)
	print('\nfor a = 0 and b = 2.4')
	print('the approximate root is',astar)
	print('the error message reads:',ier)
	print('f(astar) =', p1(astar))


	a = 0
	b = 2

	p2 = lambda x: ((x-1)**2)*(x-3)
	[astar,ier] = bisection(p2,a,b,tol, Nmax)
	print('\nfor a = 0 and b = 2')
	print('the approximate root is',astar)
	print('the error message reads:',ier)
	print('f(astar) =', p2(astar))


	a = 0
	b = 0.1
	p3 = lambda x: np.sin(x)
	[astar,ier] = bisection(p3,a,b,tol, Nmax)
	print('\nfor a = 0 and b = 0.1')
	print('the approximate root is',astar)
	print('the error message reads:',ier)
	print('f(astar) =', p3(astar))


	a = 0.5
	b = (3*np.pi)/4
	p4 = lambda x: np.sin(x)
	[astar,ier] = bisection(p4,a,b,tol, Nmax)
	print('\nfor a = 0.5 and b = (3pi)/4')
	print('the approximate root is',astar)y
	print('the error message reads:',ier)
	print('f(astar) =', p4(astar))

Problem2()


def Problem3():

	f1 = lambda x: x * (1 + (7 - x**5) / (x**2)) ** 3
	
	f2 = lambda x: x - (x**5 - 7) / x**2

	f3 = lambda x: x - (x**5 - 7) / 5 * x**4

	f4 = lambda x: x - (x**5 - 7) / 12

	Nmax = 1000
	tol = 1e-10

	x0 = 1.0
	
	[xstar,ier] = fixedpt(f1,x0,tol,Nmax)
	print('the approximate fixed point is:',xstar)
	print('f1(xstar):',f1(xstar))
	print('Error message reads:',ier)

	[xstar,ier] = fixedpt(f2,x0,tol,Nmax)
	print('the approximate fixed point is:',xstar)
	print('f2(xstar):',f2(xstar))
	print('Error message reads:',ier)

	[xstar,ier] = fixedpt(f3,x0,tol,Nmax)
	print('the approximate fixed point is:',xstar)
	print('f2(xstar):',f2(xstar))
	print('Error message reads:',ier)

	[xstar,ier] = fixedpt(f4,x0,tol,Nmax)
	print('the approximate fixed point is:',xstar)
	print('f2(xstar):',f2(xstar))
	print('Error message reads:',ier)



Problem3()

