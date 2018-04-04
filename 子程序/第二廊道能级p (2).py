import numpy as np

import matplotlib.pyplot as plt

x=np.linspace(0,16,1000)


i=50
y=np.exp(-x**2/2)*(1-x**2/2)*(1-x**2/2)


while i>0:
    #x=np.linspace(0,18,1000)
    s=1
    m=i
    n=m+1
    while n > 0:
        s = s * n
        n = n - 1
    #print s
    m1=m/2.0
    N=1/(2**m1*s**0.5)
    #print N

    dy=N**2*np.exp(-x**2/2)*x**(2*m)*(m+1-x**2/2)*(m+1-x**2/2)
    y=y+dy
    i=i-1
    
plt.plot(x,y)

plt.show()
