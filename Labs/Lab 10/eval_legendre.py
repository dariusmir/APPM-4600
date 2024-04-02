import numpy as np
import matplotlib.pyplot as plt

def eval_legendre(n, x):
    vals = np.zeros((n+1))
    vals[0] = 1
    if n > 0:
        vals[1] = x
        for i in range(2, n+1):
            vals[i] = (1/i) * ((2*(i-1)+1)*x*vals[i-1] - (i-1)*vals[i-2])
    return vals