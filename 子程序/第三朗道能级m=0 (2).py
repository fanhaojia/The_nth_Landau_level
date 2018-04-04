import numpy as np

import matplotlib.pyplot as plt

x=np.linspace(0,12,1000)



s=1
m=0
n=m
while n > 0:
    s = s * n
    n = n - 1
    #print s

m1=m/2.0
N=0.5
#print N

y=N**2*x*np.exp(-x**2/2)*(2-4*x**2/2+x**4/4)*(2-4*x**2/2+x**4/4)

plt.xlabel('r')
plt.ylabel(r'$\rho$(r)')
    
plt.plot(x,y)

plt.show()
