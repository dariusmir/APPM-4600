import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt

def driver():


    f = lambda x: 1 / (1+(10*x)**2)

    N = 3
    ''' interval'''
    a = -1
    b = 1
   
   
    ''' create equispaced interpolation nodes'''
    xint = np.linspace(a,b,N+1)
    
    ''' create interpolation data'''
    yint = f(xint)
    
    ''' create points for evaluating the Lagrange interpolating polynomial'''
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
    yeval_l= np.zeros(Neval+1)
    yeval_dd = np.zeros(Neval+1)
  
    '''Initialize and populate the first columns of the 
     divided difference matrix. We will pass the x vector'''
    y = np.zeros( (N+1, N+1) )
     
    for j in range(N+1):
       y[j][0]  = yint[j]

    y = dividedDiffTable(xint, y, N+1)
    ''' evaluate lagrange poly '''
    for kk in range(Neval+1):
       yeval_l[kk] = eval_lagrange(xeval[kk],xint,yint,N)
       yeval_dd[kk] = evalDDpoly(xeval[kk],xint,y,N)
    yeval_m = eval_monomial(f, N, Neval)

    ''' create vector with exact values'''
    fex = f(xeval)
    x = np.linspace(a,b,Neval)
    fx = f(x)
       

    plt.figure()    
    plt.plot(xeval,fex,'r--',label='Function')
    plt.plot(xeval,yeval_l,'bo--',label='Lagrange') 
    plt.plot(xeval,yeval_dd,'g--',label='Newton DD')
    plt.plot(x, yeval_m, 'k--', label='Monomial')
    plt.legend()

    plt.figure() 
    err_l = abs(yeval_l-fex)
    err_dd = abs(yeval_dd-fex)
    err_m = abs(yeval_m-fx)
    plt.semilogy(xeval,err_l,'ro--',label='Lagrange')
    plt.semilogy(xeval,err_dd,'b--',label='Newton DD')
    plt.semilogy(x,err_m, 'k--',label='Monomial')
    plt.legend()
    plt.show()


    plt.figure()
    plt.suptitle('Red:F(x), Blue:Lagrange, Green:Newton, Black:Monomial')
    p1 = 11
    p2 = 21
    u = 1
    for N in range(p1, p2):
        xint = np.linspace(a,b,N+1)

        yint = f(xint)

        Neval = 1000
        xeval = np.linspace(a,b,Neval+1)
        yeval_l= np.zeros(Neval+1)
        yeval_dd = np.zeros(Neval+1)

        y = np.zeros( (N+1, N+1) )
         
        for j in range(N+1):
           y[j][0]  = yint[j]

        y = dividedDiffTable(xint, y, N+1)

        for kk in range(Neval+1):
           yeval_l[kk] = eval_lagrange(xeval[kk],xint,yint,N)
           yeval_dd[kk] = evalDDpoly(xeval[kk],xint,y,N)
        yeval_m = eval_monomial(f, N, Neval)

        fex = f(xeval)
        x = np.linspace(a,b,Neval)
        fx = f(x)

        plt.subplot(2, 5, u)
        plt.title('N = %i' % N)
        plt.plot(xeval,fex,'ro--')
        plt.plot(xeval,yeval_l,'bo--') 
        plt.plot(xeval,yeval_dd,'g--')
        plt.plot(x, yeval_m, 'k--')
        u = u + 1

    plt.show()

    # x = np.linspace(-1, 1,N+1)

    # y = f(x)

    # Vm = np.zeros((N+1, N+1))

    # for i in range(N+1):
    #     Vm[:, i] = x**i

    # a = np.linalg.solve(Vm, y)

    # xeval = np.linspace(-1,1,Neval)
    # yeval = f(xeval)
    # Vmeval = np.zeros((Neval, N+1))
    # for i in range(0, N+1):
    #     Vmeval[:, i] = xeval**i

    # F = np.dot(Vmeval, a)
    # plt.figure()
    # plt.subplot(1, 2, 1)
    # plt.plot(xeval, yeval,)
    # plt.plot(xeval, F)
    # plt.title('True Plot Vs. Polynomial (N = 10)')

    # plt.subplot(1, 2, 2)
    # plt.semilogy(xeval, np.abs(F - yeval), 'r--')
    # plt.title('Error')
    # plt.suptitle('Monomial interpolation')
    # plt.show()

    # fl = []
    # for i in xeval:
    #     fl.append(eval_lagrange(i, x, y, N))

    # plt.figure()
    # plt.subplot(1, 2, 1)

    # plt.plot(xeval, fl)
    # plt.plot(xeval, F)
    # plt.title('True Plot vs. Polynomial (N = 10)')

    # plt.subplot(1, 2, 2)
    # plt.semilogy(xeval, np.abs(F - fl))
    
    # plt.title('Error')
    # plt.suptitle('Lagrange interpolation')
    # plt.show()
          

def eval_monomial(f, N, Neval):
    x = np.linspace(-1, 1,N+1)

    y = f(x)

    Vm = np.zeros((N+1, N+1))

    for i in range(N+1):
        Vm[:, i] = x**i

    a = np.linalg.solve(Vm, y)

    xeval = np.linspace(-1,1,Neval)
    yeval = f(xeval)
    Vmeval = np.zeros((Neval, N+1))
    for i in range(0, N+1):
        Vmeval[:, i] = xeval**i

    F = np.dot(Vmeval, a)
    monomial = np.abs(F - yeval)

    return(monomial)


def eval_lagrange(xeval,xint,yint,N):

    lj = np.ones(N+1)
    
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
              lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])

    yeval = 0.
    
    for jj in range(N+1):
       yeval = yeval + yint[jj]*lj[jj]
  
    return(yeval)
  
    


''' create divided difference matrix'''
def dividedDiffTable(x, y, n):
 
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                                     (x[j] - x[i + j]));
    return y;
    
def evalDDpoly(xval, xint,y,N):
    ''' evaluate the polynomial terms'''
    ptmp = np.zeros(N+1)
    
    ptmp[0] = 1.
    for j in range(N):
      ptmp[j+1] = ptmp[j]*(xval-xint[j])
     
    '''evaluate the divided difference polynomial'''
    yeval = 0.
    for j in range(N+1):
       yeval = yeval + y[0][j]*ptmp[j]  

    return yeval

       

driver()        
