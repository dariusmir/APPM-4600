import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
import math
from scipy.integrate import quad
from eval_chebychev import eval_chebychev


def driver():
    #  function you want to approximate
    f = lambda x: 1 / (1 + 16*x**2)

    # Interval of interest
    a = -1
    b = 1
    # weight function
    w = 1

    # order of approximation
    n = 2

    #  Number of points you want to sample in [a,b]
    N = 1000
    xeval = np.linspace(a, b, N + 1)
    pval = np.zeros(N + 1)

    for kk in range(N + 1):
        pval[kk] = eval_chebychev_expansion(f, a, b, w, n, xeval[kk])

    """ create vector with exact values"""
    fex = np.zeros(N + 1)
    for kk in range(N + 1):
        fex[kk] = f(xeval[kk])

    plt.plot(xeval, fex, label='True function')
    plt.plot(xeval, pval, label='Approximation')
    plt.title('Chebychev f(x) = 1/(1+x^2), w(x) = 1/sqrt(1-x^2)')
    plt.legend()

    err = abs(pval-fex)
    plt.figure()
    plt.semilogy(xeval, err)
    plt.title('Chebychev f(x) = 1/(1+x^2), w(x) = 1/sqrt(1-x^2) Error')
    plt.show()   


def eval_chebychev_expansion(f, a, b, w, n, x):
    #   This subroutine evaluates the Legendre expansion

    #  Evaluate all the Legendre polynomials at x that are needed
    # by calling your code from prelab
    p = eval_chebychev(n, x)
    # initialize the sum to 0
    pval = 0.0
    for j in range(0, n + 1):
        # make a function handle for evaluating phi_j(x)
        phi_j = lambda x: eval_chebychev(j, x)[-1]
        # make a function handle for evaluating phi_j^2(x)*w(x)
        phi_j_sq = lambda x: phi_j(x) ** 2 * w(x)
        # use the quad function from scipy to evaluate normalizations
        norm_fac, err = quad(phi_j_sq, a, b)
        # make a function handle for phi_j(x)*f(x)*w(x)/norm_fac
        func_j = lambda x: f(x) * phi_j(x) * w(x) / norm_fac
        # use the quad function from scipy to evaluate coeffs
        aj, err = quad(func_j, a, b)
        # accumulate into pval
        pval = pval + aj * p[j]

    return pval


if __name__ == "__main__":
    # run the drivers only if this is called from the command line
    driver()