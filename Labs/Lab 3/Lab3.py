import matplotlib.pyplot as plt
import numpy as np
from bisection import bisection
from fixedpt import fixedpt

def driver():
	# use routines
	f = lambda x: x**2*(x-1)
	a = 0.5
	b = 2
	# f = lambda x: np.sin(x)
	# a = 0.1
	# b = np.pi+0.1
	tol = 1e-7
	[astar,ier] = bisection(f,a,b,tol)
	print('the approximate root is',astar)
	print('the error message reads:',ier)
	print('\nf(astar) =', f(astar))

	a = -1
	b = 0.5
	[astar,ier] = bisection(f,a,b,tol)
	print('the approximate root is',astar)
	print('the error message reads:',ier)
	print('\nf(astar) =', f(astar))

	a = -1
	b = 2
	[astar,ier] = bisection(f,a,b,tol)
	print('the approximate root is',astar)
	print('the error message reads:',ier)
	print('\nf(astar) =', f(astar))




	a = 1
	b = 7**(1/5)
	print("\nProblem 2")
	print("\n")

	p1 = lambda x: x * (1 + (7 - x**5) / (x**2)) ** 3
	[astar,ier] = bisection(p1,a,b,tol)
	print('the approximate root is',astar)
	print('the error message reads:',ier)
	print('\nf(astar) =', f(astar))


	p2 = lambda x: x - (x**5 - 7) / x**2
	[astar,ier] = bisection(p1,a,b,tol)
	print('the approximate root is',astar)
	print('the error message reads:',ier)
	print('\nf(astar) =', f(astar))


	p3 = lambda x: x - (x**5 - 7) / 5 * x**4
	[astar,ier] = bisection(p1,a,b,tol)
	print('the approximate root is',astar)
	print('the error message reads:',ier)
	print('\nf(astar) =', f(astar))


	p4 = lambda x: x - (x**5 - 7) / 12
	[astar,ier] = bisection(p1,a,b,tol)
	print('the approximate root is',astar)
	print('the error message reads:',ier)
	print('\nf(astar) =', f(astar))

#driver()

def driver3():

# test functions 
	f1 = lambda x: x * (1 + (7 - x**5) / (x**2)) ** 3
	
	f2 = lambda x: x - (x**5 - 7) / x**2

	f3 = lambda x: x - (x**5 - 7) / 5 * x**4

	f4 = lambda x: x - (x**5 - 7) / 12

	Nmax = 1000
	tol = 1e-2
	#tol2 = 1e-13

# test f1 '''
	x0 = 1.0
	[xstar,ier] = fixedpt(f1,x0,tol,Nmax)
	print('the approximate fixed point is:',xstar)
	print('f1(xstar):',f1(xstar))
	print('Error message reads:',ier)

	#test f2 '''
	x0 = 1.0
	[xstar,ier] = fixedpt(f2,x0,tol,Nmax)
	print('the approximate fixed point is:',xstar)
	print('f2(xstar):',f2(xstar))
	print('Error message reads:',ier)

	x0 = 1.0
	[xstar,ier] = fixedpt(f3,x0,tol,Nmax)
	print('the approximate fixed point is:',xstar)
	print('f2(xstar):',f2(xstar))
	print('Error message reads:',ier)

	x0 = 1.0
	[xstar,ier] = fixedpt(f4,x0,tol,Nmax)
	print('the approximate fixed point is:',xstar)
	print('f2(xstar):',f2(xstar))
	print('Error message reads:',ier)


	f5 = x**4 - 3*x**2 - 3
	x0 = 1.0
	[xstar,ier] = fixedpt(f4,x0,tol,Nmax)
	print('the approximate fixed point is:',xstar)
	print('f2(xstar):',f2(xstar))
	print('Error message reads:',ier)


driver3()

