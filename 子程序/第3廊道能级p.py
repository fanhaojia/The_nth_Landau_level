import numpy as np
from decimal import *
from math import *
import matplotlib.pyplot as plt
x=np.linspace(0,20,1000)
with localcontext() as ctx:
    ctx.prec = 32 
    i=50
    y=0.25*ctx.exp(-x**2/2)*(2-4*x**2/2+x**4/4)*(2-4*x**2/2+x**4/4)+0.125*x**4*ctx.exp(-x**2/2)+0.25*x**2*ctx.exp(-x**2/2)*(2-x**2/2)*(2-x**2/2)

    while i>0:
    
        s=1
        m=i
        n=m
        while n > 0:
            s = s * n
            n = n - 1
    
    
        N=1.0/(-(m+2)**2*(m+1)**2*2**m*s+(m+2)**3*(m+1)*2**(m+2)*s-(m+3)*(m+2)**2*(m+1)*2**(m+2)*s+2**m*(m+4)*(m+3)*(m+2)*(m+1)*s)
    
        dy=N*ctx.exp(-x**2/2)*x**(2*m)*((m+2)*(m+1)-2*(m+2)*x**2/2+x**4/4)*((m+2)*(m+1)-2*(m+2)*x**2/2+x**4/4)
        y=y+dy
        i=i-1
plt.xlabel('x')
plt.ylabel(r'$\rho$(x)')
plt.plot(x,y)
plt.show()
