import numpy as np

import matplotlib.pyplot as plt

x=np.linspace(0,20,1000)

i=20
#y=0
y=0.25*np.exp(-x**2/2)*(2-4*x**2/2+x**4/4)*(2-4*x**2/2+x**4/4)+0.125*x**4*np.exp(-x**2/2)+0.25*x**2*np.exp(-x**2/2)*(2-x**2/2)*(2-x**2/2)


while i>0:
    
    a=0 #积分上限
    b=50.0 #积分下限
    nr=0
    m=i
    width=0.0001 #步长
    N=Get_N(a,b,width)
    datas = GenerateData(a,b,N,width)
    xishu=1.0/simpson_integral(datas,width,N)

    dy=xishu*np.exp(-x**2/2)*x**(2*m)*((m+2)*(m+1)-2*(m+2)*x**2/2+x**4/4)*((m+2)*(m+1)-2*(m+2)*x**2/2+x**4/4)
    y=y+dy
    i=i-1
plt.xlabel('x')
plt.ylabel(r'$\rho$(x)')
plt.plot(x,y)

plt.show()
