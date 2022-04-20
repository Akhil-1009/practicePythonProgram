# create a program that asks the user for a number and then prints out a list of all the divisor of that number
a=int(input("enter a number for check"))
for i in range(1,(a//2)+1):
    if(a%i==0):
        print(i)
else:
    print(a)