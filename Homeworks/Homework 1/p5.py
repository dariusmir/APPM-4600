import matplotlib.pyplot as plt
import numpy as np

#Problem 5b
x = np.pi

delta = np.logspace(-16, 0, 17)

x1 = lambda d : np.cos(x + d) - np.cos(x)
x2 = lambda d : -2 * np.sin(x + d / 2) * np.sin(d / 2)

y1 = x1(delta)
y2 = x2(delta)

deltaY = y1 - y2

plt.plot(delta, deltaY)

plt.xscale('log')
plt.xlabel('delta')
plt.ylabel('delta y')
plt.title('x = 3.14, 5b')

plt.show()


x = 10**6

x1 = lambda delt : np.cos(x + delt) - np.cos(x)
x2 = lambda delt : -2 * np.sin(x + delt / 2) * np.sin(delt / 2)

y1 = x1(delta)
y2 = x2(delta)

deltaY = y1 - y2

plt.plot(delta, deltaY)

plt.xscale('log')
plt.xlabel('delta')
plt.ylabel('delta y')
plt.title('x = 10^6, 5b')

plt.show()






#Problem 5 C
x = np.pi
def algo(delta):
	return (-delta * np.sin(x + delta) + np.sin(x)) / np.math.factorial(len(delta))

y1 = x2(delta)
y2 = algo(delta)


deltaY = np.abs(y2- y1)
plt.plot(delta, deltaY)


plt.xscale('log')
plt.yscale('log')

plt.xlabel('Delta')
plt.ylabel('Delta y')

plt.title('x = 3.14, 5C')

plt.show()


x = 10**6

y1 = x2(delta)
y2 = algo(delta)

deltaY = np.abs(y2- y1)

plt.plot(delta, deltaY)

plt.xscale('log')
plt.yscale('log')

plt.xlabel('Delta')
plt.ylabel('Delta y')

plt.title('x = 10^6, 5C')

plt.show()


