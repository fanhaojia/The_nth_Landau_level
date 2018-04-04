import numpy as np

import matplotlib.pyplot as plt

x=np.linspace(0,14,1000)

m=40
s=1
n=m
while n > 0:
        s = s * n
        n = n - 1
#print s
N=1.0/(-((m+2)**2)*((m+1)**2)*(2**m)*s+((m+2)**3)*(m+1)*(2**(m+2))*s-(m+3)*((m+2)**2)*(m+1)*(2**(m+2))*s+(2**m)*(m+4)*(m+3)*(m+2)*(m+1)*s)
#print N   
y=N*np.exp(-x**2/2)*x**(2*m)*((m+2)*(m+1)-2*(m+2)*x**2/2+x**4/4)*((m+2)*(m+1)-2*(m+2)*x**2/2+x**4/4)

plt.xlabel('x')
plt.ylabel(r'$\rho$(x)')
plt.plot(x,y)

plt.show()
