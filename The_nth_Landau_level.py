#调节nr，就可获得第nr朗道能级
#!/usr/bin/python
# Author: Missa
#coding = utf-8
"simpson 法计算积分，数值积分，效果非常理想"
from math import *
import numpy as np
import matplotlib.pyplot as plt

def func1(z):
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
def GenerateData1(a,b,n,width):
    datas1 = []
    r=a
    for i in range(0,n):
        datas1.append(func1(r))
        r = r+width
    return datas1
def simpson_integral1(datas1,width,n):
    sum = datas1[0]+datas1[n-1]
    for i in range(2,n):
        if i%2== 0:
            sum = sum +4*datas1[i-1]
        else:
            sum = sum +2*datas1[i-1]
    return sum*width/3.0


if __name__ == "__main__":
    t=50#’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’m的最大值
    nr=40#“‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’‘’第nr朗道能级
    a=0 #积分上限
    b=50.0 #积分下限
    width=0.0001 #步长
    N=Get_N(a,b,width)
    x=np.linspace(0,25,1000)
    j = [1]*nr
    p = [1]*nr
    for i in range(0,nr):
        p[i]=i
        j[i]=nr-i
    f=[1.0]*nr
    y=0
    for i in range(0,nr):
        datas2=[]
        r=a
        for h in range(0,N):
            z=r**(2.0*j[i]+1)*np.exp(-r**2/2)*hlcjh(-p[i],j[i]+1,r**2/2)**2
            datas2.append(z)
            r = r+width
        sum = datas2[0]+datas2[N-1]
        for k in range(2,N):
            if k%2== 0:
                sum = sum +4*datas2[k-1]
            else:
                sum = sum +2*datas2[k-1]
        xishu2=1.0/(sum*width/3.0)
        print i
        f[i]=xishu2*x**(2.0*j[i])*np.exp(-x**2/2)*hlcjh(-p[i],j[i]+1,x**2/2)**2
        y=y+f[i]
    while t>=0:
        m=t
        datas1 = GenerateData1(a,b,N,width)
        xishu1=1.0/simpson_integral1(datas1,width,N)
        print xishu1
        dy=xishu1*np.exp(-x**2/2)*x**(2*m)*hlcjh(-nr,m+1,x**2/2)**2
        y=y+dy
        t=t-1
plt.xlabel('r')
plt.ylabel(r'$\rho$(r)')
plt.plot(x,y)
plt.show()
