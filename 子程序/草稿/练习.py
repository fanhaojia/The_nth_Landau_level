#coding = utf-8#simpson 法计算积分，数值积分，效果非常理想
from math import *
def func(x):
    """ 定义被积分函数 """
    return x*sin(x)
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
    b=30.0 #积分下限
    width=0.0625 #步长
    N=Get_N(a,b,width)
    datas = GenerateData(a,b,N,width)
print simpson_integral(datas,width,N)
