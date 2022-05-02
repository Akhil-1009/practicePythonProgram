# from tkinter.tix import InputOnly
# def user_input():
#     a=input("enter the value ")
#     b=input("enter the value")
#     return (a,b)
# def add(a,b):
#     return a+b
# a,b=user_input()
# add(a,b)
# print(a,'+',b,'=',add(a,b))
# a,b=int(input("enter the values"))
count=1
def plus():
    global count
    count+=1
def minus():
    global count
    count-=1
print("count =",count)
plus()
plus()
minus()
minus()
print("count =",count)