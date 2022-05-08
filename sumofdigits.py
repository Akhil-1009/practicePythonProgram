num=int(input("enter the number"))
sum=0
while(num!=0):
    digit=num%10
    sum+=digit
    num=num//10
print("the sum is",sum)
