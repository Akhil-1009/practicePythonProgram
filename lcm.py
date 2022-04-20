print("program for lcm of three no")
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
def lcm1(a,b,c):
    for i in range(1,a*b*c+1):
        if((i%a==0)and(i%b==0)and(i%c==0) ):
            print("LCM OF ",a,b,c,"is ",i)
            break
lcm1(a,b,c)
