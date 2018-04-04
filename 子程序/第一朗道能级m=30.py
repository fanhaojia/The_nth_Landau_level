import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,14,1000)
i=30
y=0
while i>=0:
    s=1
    m=i
    n=m
    while n > 0:
        s = s * n
        n = n - 1
    #print s
    m1=m/2.0
    N=1/(2**m1*s**0.5)
    #print N
    y=N**2*np.exp(-x**2/2)*x**(2*m+1)
    i=i-1
    plt.plot(x,y)
plt.xlabel('r')
plt.ylabel(r'$\rho$(r)')

plt.show()
