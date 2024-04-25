import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 
from numpy.linalg import norm
import scipy


def driver():

    x = 2
    f = lambda t: t**(x-1)*np.e**(-t)
    a = 0
    b = 100000
    
    I_ex = 1
    
    n = 1000000
    I_trap = compositeTrapezoid(a,b,n,f)
    print('I_trap= ', I_trap)
    
    err = abs(I_ex-I_trap)   
    
    print('absolute error = ', err)

    I_scipy = scipy.special.gamma(x)

    print('The scipy argument gets:', I_scipy)

    err = abs(I_ex - I_scipy)

    print('The scipy error is:', err)
    
    I_simp = compositeSimpsons(a,b,n,f)

    print('I_simp= ', I_simp)
    
    err = abs(I_ex-I_simp)   
    
    print('absolute error = ', err)    

        
def compositeTrapezoid(f, a, b, n):
    h = (b - a) / n
    sum = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        sum += 2 * f(x)
    return sum * h / 2


def compositeSimpsons(f, a, b, n):
    if n % 2 == 1:
        n += 1
    h = (b - a) / n
    sum = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            sum += 2 * f(x)
        else:
            sum += 4 * f(x)
    return sum * h / 3


    
    
driver()    