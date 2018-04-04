import numpy as np

import matplotlib.pyplot as plt

x=np.linspace(0,10,1000)


y1=0.5*np.exp(-x**2/2)*(4-4*x**2/2+x**4/4)*(4-4*x**2/2+x**4/4)+0.125*x**4*np.exp(-x**2/2)+0.25*x**2*np.exp(-x**2/2)*(2-x**2/2)*(2-x**2/2)

plt.xlabel('x')
plt.ylabel(r'$\rho$(x)')
plt.plot(x,y1)

plt.show()

