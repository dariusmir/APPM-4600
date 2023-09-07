import matplotlib.pyplot as plt
import numpy as np

xPt = np.arange(1.920,2.081,0.001)

p = lambda x : x**9 - 18*x**8 + 144*x**7 - 672*x**6 + 2016*x**5 - 4032*x**4 + 5376*x**3 - 4608*x**2 + 2304*x - 512
y = p(xPt)
plt.plot(xPt, y, label='Evaluating p via its coefficients')

p = lambda x : (x - 2)**9
y = p(xPt)
plt.plot(xPt, y, label='Evaluating p using the exact expression')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()

plt.show()