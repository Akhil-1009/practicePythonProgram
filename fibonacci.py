print("program for fibonacci series")
no=int(input("enter no upto which print the series"))
a=0
b=1
print(a)
print(b)
for i in range(0,no-2):
    sum=a+b
    print(sum)
    a=b
    b=sum
 