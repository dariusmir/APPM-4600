import numpy as np

f = lambda x: np.cos(x)
h = 0.01 * 2.**(-np.arange(0,10))

s = np.pi/2
fd = (f(s + h) - f(s)) / h
print(fd)

cd = (f(s + h) - f(s - h))/(2 * h)
print(cd)

print('Both have linear orders of convergence')