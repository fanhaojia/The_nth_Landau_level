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
    x=np.linspace(0,25,1000)
    j1=50
    j2=49
    j3=48
    j4=47
    j5=46
    j6=45
    j7=44
    j8=43
    j9=42
    j10=41
    j11=40
    j12=39
    j13=38
    j14=37
    j15=36
    j16=35
    j17=34
    j18=33
    j19=32
    j20=31
    j21=30
    j22=29
    j23=28
    j24=27
    j25=26
    j26=25
    j27=24
    j28=23
    j29=22
    j30=21
    j31=20
    j32=19
    j33=18
    j34=17
    j35=16
    j36=15
    j37=14
    j38=13
    j39=12
    j40=11
    j41=10
    j42=9
    j43=8
    j44=7
    j45=6
    j46=5
    j47=4
    j48=3
    j49=2
    j50=1
    y1= 2.3337291662e-17*x**(2*j1)*np.exp(-x**2/2)*hlcjh(0,j1+1,x**2/2)**2
    y2= 1.05017812479e-14*x**(2*j2)*np.exp(-x**2/2)*hlcjh(-1,j2+1,x**2/2)**2
    y3= 2.05834912459e-12*x**(2*j3)*np.exp(-x**2/2)*hlcjh(-2,j3+1,x**2/2)**2
    y4= 2.31907334704e-10*x**(2*j4)*np.exp(-x**2/2)*hlcjh(-3,j4+1,x**2/2)**2
    y5= 1.66973280987e-08*x**(2*j5)*np.exp(-x**2/2)*hlcjh(-4,j5+1,x**2/2)**2
    y6= 8.08150679976e-07*x**(2*j6)*np.exp(-x**2/2)*hlcjh(-5,j6+1,x**2/2)**2
    y7= 2.69383559992e-05*x**(2*j7)*np.exp(-x**2/2)*hlcjh(-6,j7+1,x**2/2)**2
    y8= 0.000623430524553*x**(2*j8)*np.exp(-x**2/2)*hlcjh(-7,j8+1,x**2/2)**2
    y9= 0.00997488839284*x**(2*j9)*np.exp(-x**2/2)*hlcjh(-8,j9+1,x**2/2)**2
    y10= 0.108615451389*x**(2*j10)*np.exp(-x**2/2)*hlcjh(-9,j10+1,x**2/2)**2
    y11= 0.782031249999*x**(2*j11)*np.exp(-x**2/2)*hlcjh(-10,j11+1,x**2/2)**2
    y12= 3.55468749999*x**(2*j12)*np.exp(-x**2/2)*hlcjh(-11,j12+1,x**2/2)**2
    y13= 9.47916666665*x**(2*j13)*np.exp(-x**2/2)*hlcjh(-12,j13+1,x**2/2)**2
    y14= 13.125*x**(2*j14)*np.exp(-x**2/2)*hlcjh(-13,j14+1,x**2/2)**2
    y15= 7.5*x**(2*j15)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y16=  *x**(2*j16)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y17=  *x**(2*j17)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y18=  *x**(2*j18)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y19=  *x**(2*j19)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y20=  *x**(2*j20)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y21=  *x**(2*j21)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y22=  *x**(2*j22)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y23=  *x**(2*j23)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y24=  *x**(2*j24)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y25=  *x**(2*j25)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y26=  *x**(2*j26)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y27=  *x**(2*j27)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y28=  *x**(2*j28)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y29=  *x**(2*j29)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y30=  *x**(2*j30)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y31=  *x**(2*j31)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y32=  *x**(2*j32)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y33=  *x**(2*j33)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y34=  *x**(2*j34)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y35=  *x**(2*j35)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y36=  *x**(2*j36)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y37=  *x**(2*j37)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y38=  *x**(2*j38)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y39=  *x**(2*j39)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y40=  *x**(2*j40)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y41=  *x**(2*j41)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y42=  *x**(2*j42)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y43=  *x**(2*j43)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y44=  *x**(2*j44)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y45=  *x**(2*j45)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y46=  *x**(2*j46)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y47=  *x**(2*j47)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y48=  *x**(2*j48)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y49=  *x**(2*j49)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    y50=  *x**(2*j50)*np.exp(-x**2/2)*hlcjh(-14,j15+1,x**2/2)**2
    
    y=y1+y2+y3+y4+y5+y6+y7+y8+y9+y10+y11+y12+y13+y14+y15
    while i>=0:
        a=0 #积分上限
        b=50.0 #积分下限
        width=0.0001 #步长
        N=Get_N(a,b,width)
        nr=15
        m=i
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

