# SWAPPING PROGRAM
print("this script is intended to swap the vaues of two data variable using a third temporary variable")
a=input("enter first number ")
b=input("enter second number ")
print("before swapping data variables ",a,b)
c=a
a=b
b=c
print("after swapping data variables is",a," ",b," ")
# TARIKA 2
print("before swapping data variables ",a,b)

a=a+b
b=a-b
a=a-b
print("after swapping data variables is",a," ",b," ")


# TARIKA 3
print("before swapping data variables ",a,b)
a,b=b,a
print("after swapping data variables is",a," ",b," ")
