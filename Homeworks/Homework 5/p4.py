import matplotlib.pyplot as plt
import numpy as np

a0, a1 = 1.3, 1.3

x = np.array([0, 1, 2, 3])
y = np.array([1, 4, 2, 6])

plt.scatter(x, y, label='Data Points')

x_range = np.linspace(min(x), max(x), 100)

p = a1*x_range + a0
plt.plot(x_range, p, label="Unweighted")

w = np.array([1, 4, 9, 6])

D = np.diag(np.sqrt(w))

M = np.vstack([np.ones_like(x), x]).T

y_vec = y[:, np.newaxis]

MTDM = M.T @ D @ M
MTDy = M.T @ D @ y_vec

a_weight = np.linalg.solve(MTDM, MTDy)
a0_weight, a1_weight = a_weight.flatten()

p_weight = a1_weight * x_range + a0_weight
plt.plot(x_range, p_weight, 'g--', label='Weighted Least Squares')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of Linear Fits')
plt.legend()
plt.grid(True)
plt.show()