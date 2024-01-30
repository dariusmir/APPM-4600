import matplotlib.pyplot as plt
import numpy as np

#Plotting using plt and numpy
X = np.linspace(0, 2 * np.pi, 100)
Ya = np.sin(X)
Yb = np.cos(X)
plt.plot(X, Ya)
plt.plot(X, Yb)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
