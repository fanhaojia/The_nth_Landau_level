import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,20,1000)
i=50
y=np.exp(-x**2/2)+np.exp(-x**2/2)*(1-x**2/2)*(1-x**2/2)+0.5*x**2*np.exp(-x**2/2)
while i>0:
    s=1
    s2=1
    m=i
    n=m
    n2=m+1
    while n > 0:
        s = s * n
        n = n - 1
    while n2 > 0:
        s2 = s2 * n2
        n2 = n2 - 1
    #print s
    m1=m/2.0
    N1=1.0/(2**m1*s**0.5)
    N2=1.0/(2**m1*s2**0.5)
    
    dy1=N1**2*np.exp(-x**2/2)*x**(2*m)
    dy2=N2**2*np.exp(-x**2/2)*x**(2*m)*(m+1-x**2/2)*(m+1-x**2/2)
    
    y=y+dy1+dy2
    i=i-1    
plt.xlabel('r')
plt.ylabel(r'$\rho$(r)')
plt.plot(x,y)
plt.show()
