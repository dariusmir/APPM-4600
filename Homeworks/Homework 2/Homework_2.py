import numpy as np
import matplotlib.pyplot as plt
import math

def PartA():
	t = np.linspace(0, math.pi, 30)
	y = np.cos(t)

	S = 0

	for i in range(30):
		S = S + t[i]*y[i]

	print("the sum is: ", S)

def PartB():
	R = 1.2
	delR = 0.1
	f = 15
	p = 30

	theta = np.linspace(0, 2*np.pi, 500)

	xtheta = R*(1+delR*np.sin(f*theta+p))*np.cos(theta)
	ytheta = R*(1+delR*np.sin(f*theta+p))*np.sin(theta)

	plt.plot(xtheta, ytheta)
	plt.show()
	plt.savefig('4b1')

	p  = np.random.uniform(0,2,1)
	delR = 0.05

	for i in range(10):
		R = i
		f = 2 + i
		xtheta = R*(1+delR*np.sin(f*theta+p))*np.cos(theta)
		ytheta = R*(1+delR*np.sin(f*theta+p))*np.sin(theta)
		plt.plot(xtheta, ytheta)

	plt.show()
	plt.savefig('4b2')

PartB()

