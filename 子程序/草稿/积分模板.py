#coding = utf-8
"simpson 法计算积分，数值积分，效果非常理想"
from math import *
import numpy as np
def func(x):
    """ 定义被积分函数 """
    j1=15
    j2=14
    j3=13
    j4=12
    j5=11
    j6=10
    j7=9
    j8=8
    j9=7
    j10=6
    j11=5
    j12=4
    j13=3
    j14=2
    j15=1
    
    return x**(2*j11+1)*np.exp(-x**2/2)*hlcjh(-10,j11+1,x**2/2)**2

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
    a=0 #积分上限
    b=50.0 #积分下限
    width=0.0001 #步长
    N=Get_N(a,b,width)
    datas = GenerateData(a,b,N,width)
    xishu=1.0/simpson_integral(datas,width,N)
    print xishu
