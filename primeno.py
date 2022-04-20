from tkinter.messagebox import YES

print("program to check whether a no is prime or not")
no=int(input("enter a no"))
flag="yes"
if(no>=2):
    for i in range(2,no):
        if(no%i==0):
            print(no," is not prime")
            break
    else:
         print(no,"is prime no")
else:
    print("invalid value")