# area with function overloading
def area(radius):
    return 3.14*radius*radius
def area(l,b):
    return l*b
r=int(input("enter the radius"))
l=int(input("enter the length"))
b=int(input("enter the breadth"))
print("the area of circle is",area(r))
print("the area of rectangle is",area(l,b))