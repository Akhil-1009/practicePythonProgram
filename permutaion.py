print("program for permutaion of a no")
n=int(input("enter the value of n"))
r=int(input("enter the value of r"))
temp=n-r
def fact(n):
    fact_n=1
    for i in range(1,n+1):
        fact_n*=i
    print("factorial of ",n,"is =",fact_n)
    return fact_n
result=fact(n)//fact(temp)
print("the result of permutation is",result)
# without function ////
# fact1=1
# fact2=1
# if(n>0):
#     for i in range(1,n+1):
#         fact1=fact1*i
# if(temp>0):
#     for i in range(1,temp+1):
#         fact2=fact2*i
# ans=fact1//fact2
# print("the permutation is : ",ans)