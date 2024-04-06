import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import norm

def driver():
    f = lambda x: np.sin(9*x)
    a = 0
    b = 1

    N_points = [5, 10, 20, 40]

    for N in N_points:
        ''' create equispaced points'''
        xint = np.linspace(a, b, N+1)
        yint = f(xint)

        ''' create points you want to evaluate at'''
        Neval = 10000
        xeval = np.linspace(xint[0], xint[N], Neval+1)

        (M, C, D) = create_natural_spline(yint, xint, N)

        yeval = eval_cubic_spline(xeval, Neval, xint, N, M, C, D)

        ''' evaluate f at the evaluation points'''
        fex = f(xeval)

        err = abs(yeval - fex)
        log_err = np.log10(err)

        plt.figure()
        plt.plot(xeval, log_err, label='N={}'.format(N))
        plt.xlabel('x')
        plt.ylabel('Logarithm of Interpolation Error')
        plt.title('Logarithm of Interpolation Error for N={}'.format(N))
        plt.legend()
        plt.show()

def create_natural_spline(yint, xint, N):
    # create the right  hand side for the linear system
    b = np.zeros(N+1)
    # vector values
    h = np.zeros(N+1)
    for i in range(1, N):
        hi = xint[i] - xint[i-1]
        hip = xint[i+1] - xint[i]
        b[i] = (yint[i+1] - yint[i]) / hip - (yint[i] - yint[i-1]) / hi
        h[i-1] = hi
        h[i] = hip

    # create matrix so you can solve for the M values
    A = np.identity(N+1)

    for i in range(1, N):
        A[i][i - 1] = h[i - 1] / 3
        A[i][i] = (h[i - 1] + h[i]) / 3
        A[i][i + 1] = h[i] / 3

    Ainv = np.linalg.inv(A)

    M = Ainv @ b

    # Create the linear coefficients
    C = np.zeros(N)
    D = np.zeros(N)
    for j in range(N):
        C[j] = yint[j] / h[j] - h[j] * M[j] / 6
        D[j] = yint[j + 1] / h[j] - h[j] * M[j + 1] / 6
    return M, C, D

def eval_local_spline(xeval, xi, xip, Mi, Mip, C, D):
    # Evaluates the local spline
    hi = xip - xi
    yeval = 1 / hi * (-Mi * (xeval - xip) ** 3 / 6 + Mip * (xeval - xi) ** 3 / 6) - C * (xeval - xip) + D * (xeval - xi)
    return yeval

def eval_cubic_spline(xeval, Neval, xint, Nint, M, C, D):
    yeval = np.zeros(Neval + 1)

    for j in range(Nint):
        atmp = xint[j]
        btmp = xint[j + 1]

        ind = np.where((xeval >= atmp) & (xeval <= btmp))
        xloc = xeval[ind]

        yloc = eval_local_spline(xloc, atmp, btmp, M[j], M[j + 1], C[j], D[j])
        yeval[ind] = yloc

    return yeval

driver()