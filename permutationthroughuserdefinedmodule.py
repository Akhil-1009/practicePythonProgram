# from math import lcm
import factorial
x=int(input("enter the first number"))
y=int(input("enter the second number"))
temp=x-y
result=factorial.facto(x)//factorial.facto(temp)
print(result)