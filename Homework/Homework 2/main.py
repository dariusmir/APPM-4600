import matplotlib.pyplot as plt
import numpy as np
import math

t = np.linspace(0, np.pi, 30)
y = np.cos(t)
tot = 0
for i in range(len(t)):
    tot += (t[i] * y[i])


print("The sum is: ", tot)

theta = np.linspace(0, 2*np.pi, 500)

R = 1.2
delta_r = 0.1
f = 15
p = 0

x = R * (1 + delta_r * np.sin(f*theta+p)) * np.cos(theta)
y = R * (1 + delta_r * np.sin(f*theta+p)) * np.sin(theta)

plt.plot(x, y)
plt.xlabel('x')
plt.xlabel('y')
#plt.save('4B, Figure 1')
plt.show()
flag = True

for i in range(1, 11):
	R = i
	delta_r = 0.05
	f = 2 + i
	p = np.random.uniform(0, 2)

	x = R * (1 + delta_r * np.sin(f*theta + p)) * np.cos(theta)
	y = R * (1 + delta_r * np.sin(f*theta + p)) * np.sin(theta)
	plt.plot(x, y)

plt.xlabel('x')
#plt.save('4B, Figure 2')
plt.xlabel('y')
plt.show()