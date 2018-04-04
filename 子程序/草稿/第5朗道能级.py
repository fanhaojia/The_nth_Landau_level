#coding = utf-8
"simpson 法计算积分，数值积分，效果非常理想"
from math import *
import numpy as np
import matplotlib.pyplot as plt
def func(z):
    """ 定义被积分函数 """
    x=hlcjh(-nr,m+1,z**2/2)
    
    return (z**m*x*exp(-z**2/4))**2*z
def hlcjh(a,b,c):
    g=1
    ra=-a+1
    s1=1.0
    s2=1.0
    s3=1.0
    if a<0:
        for i in range(1,ra):
            s1=s1*i
            s2=s2*b
            s3=s3*a
            b=b+1
            a=a+1
            dg=c**i*s3/(s1*s2)
            
            g=g+dg
    else:
        g=1
    return g
def Get_N(a,b,width): # width为步长
    N=int((b-a)/width + 1)
    if N%2 == 0:
        N=N+1
    return N
def GenerateData(a,b,n,width):
    datas = []
    r=a
    for i in range(0,n):
        datas.append(func(r))
        r = r+width
    return datas
def simpson_integral(datas,width,n):
    sum = datas[0]+datas[n-1]
    for i in range(2,n):
        if i%2== 0:
            sum = sum +4*datas[i-1]
        else:
            sum = sum +2*datas[i-1]
    return sum*width/3.0
if __name__ == "__main__":
    i=100
    x=np.linspace(0,20,1000)
    j1=4
    j2=3
    j3=2
    j4=1
    y1= 0.00260416666667*x**(2*j1)*np.exp(-x**2/2)*hlcjh(0,j1+1,x**2/2)**2
    y2= 0.0833333333334*x**(2*j2)*np.exp(-x**2/2)*hlcjh(-1,j2+1,x**2/2)**2
    y3= 0.75*x**(2*j3)*np.exp(-x**2/2)*hlcjh(-2,j3+1,x**2/2)**2
    y4= 2.0*x**(2*j4)*np.exp(-x**2/2)*hlcjh(-3,j4+1,x**2/2)**2
    y=y1+y2+y3+y4
    while i>=0:
        a=0 #积分上限
        b=50.0 #积分下限
        width=0.0001 #步长
        N=Get_N(a,b,width)
        nr=4
        m=i
        width=0.001 #步长
        N=Get_N(a,b,width)
        datas = GenerateData(a,b,N,width)
        xishu=1.0/simpson_integral(datas,width,N)
        print xishu
        dy=xishu*np.exp(-x**2/2)*x**(2*m)*hlcjh(-nr,m+1,x**2/2)**2
        y=y+dy
        i=i-1
    plt.xlabel('r')
    plt.ylabel(r'$\rho$(r)')
    plt.plot(x,y)
    plt.show()

