#合流超几何函数多项式

from math import *
def hlcjh(a,b,c):
    f=0
    ra=-a
    s1=1
    s2=1
    s2=1
    if a<0:
        for i in range(1,ra):
            s1=s*i
            s2=s2*b
            s3=s3*a
            b=b+1
            a=a+1
            df=s3/(s1*s2)*c**i
            
            f=f+df
    else:
        f=1
    return f
if __name__ == "__main__":
    a=-1
    b=2
    c=2
    f= hlcjh(a,b,c)
    print(f)


