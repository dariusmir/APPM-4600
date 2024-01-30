import matplotlib.pyplot as plt
import numpy as np

#Lab 1
x = np.linspace(1,10,10)
y = np.arange(1., 11., 1)

print(x)
print(y)

print('The first three entries are ', x[0:3])

w = 10**(-np.linspace(1,10,10))
s = w*3
print(w)
print(s)

plt.semilogy(x, w, label='w')
plt.semilogy(x,s, label='s')
plt.xlabel('x')
plt.ylabel('w')
plt.legend()
plt.show()