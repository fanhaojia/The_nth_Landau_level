#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
#from math import*
import math

r=np.linspace(0,10,1000)
n=4
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
        return s

m=1
s=1
N=1/(np.sqrt(power(2,m)*s))
print N


y=N*power(r,m)*power(math.e,-r*r/4)



plt.plot(r,y)

import numpy as np

import matplotlib.pyplot as plt

x=np.linspace(0,10,1000)

m=1
s=1
N=1/(np.sqrt(2**m*s))

y=N**2*np.exp(-x**2/2)*x**(2*m+1)


plt.plot(x,y)

plt.show()
