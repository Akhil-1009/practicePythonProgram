from support import *
a=int(input("enter the value of a : "))
b=int(input("enter the value of b : "))
def smart_div(funct):
    def inner_div(m,n):
        if(m<n):
            m,n=n,m
        return funct(m,n)
    return inner_div
c=div(a,b)
div1=smart_div(div)
d=div1(a,b)
print("a =",a)
print("b =",b)
print("c ",c)
