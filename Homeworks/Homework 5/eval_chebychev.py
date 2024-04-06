import numpy as np
import matplotlib.pyplot as plt

def eval_chebychev(n, x):

    vals = np.zeros(n+1)
    vals[0] = 1
    if n >= 1:
        vals[1] = x

    for i in range(2, n+1):
        vals[i] = 2 * x * vals[i-1] - vals[i-2]

    return vals