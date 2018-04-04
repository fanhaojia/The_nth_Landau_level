import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,1000)
y=np.exp(-x**2/2)*x
plt.xlabel('r')
plt.ylabel(r'$\rho$(r)')
plt.plot(x,y)
plt.show()
