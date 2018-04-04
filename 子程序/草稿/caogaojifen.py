from math import *
def hlcjh(a,b,c):
    g=1
    ra=-a+1
    s1=1.0
    s2=1.0
    s3=1.0
    if a<0:
        for i in range(1,ra):
            
            s1=s1*i
            print s1
            s2=s2*b
            print s2
            s3=s3*a
            print s3
            b=b+1
            a=a+1
            print c
            dg=c**i*s3/(s1*s2)
            print dg
            
            g=g+dg
    else:
        g=1
    return g
if __name__ == "__main__":
    a=0
    b=1
    c=3
    y=hlcjh(a,b,c)
    print y
