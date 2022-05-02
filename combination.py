n=int(input("enter the value of n"))
r=int(input("enter the value of r"))
temp=n-r
def fact(n):
    fact_n=1
    for i in range(1,n+1):
        fact_n*=i
    print("factorial of ",n,"is =",fact_n)
    return fact_n
result=fact(n)//(fact(temp)*fact(r))
print("the result of combination is",result)