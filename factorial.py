# factorial of a number 



no=int(input("enter a number for factorial"))
def facto(no):
    fact=1
    for i in range(1,no+1):
        fact=fact*i
    return fact
# print(facto(no))    