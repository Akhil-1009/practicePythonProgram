print(" program for greater of three no")
a=int(input("enter first number"))
b=int(input("enter first number"))
c=int(input("enter first number"))

if(a==b==c):    
    print("all are equal no")
elif(a>b)and(a>c):
    print(a,"is greater number of three")
elif((b>c)and(b>a)):
    print(b,"b is greater no")
elif((c>a)and(c>b)):
     print(c," is greater no")
elif(((a==b)or(a==c))and((a>c)or(a>b))):
    print(a,"is greater no")
elif(((b==a)or(b==c))and((b>a)or(b>c))):
    print(b,"is greater no")
else:
    print(c,"is greater no")


