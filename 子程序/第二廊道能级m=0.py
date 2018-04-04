import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,14,1000)
y=np.exp(-x**2/2)*(1-x**2/2)*(1-x**2/2)*x##+0.5*x**2*np.exp(-x**2/2)
plt.xlabel('r')
plt.ylabel(r'$\rho$(r)')
plt.plot(x,y)
plt.show()
