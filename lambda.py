# lambda function
from functools import reduce


z = lambda x,y : x+y
print(z(2,4))

list1=[2,13,42,4,524,331,452,321,22]
list_even=[]
# print(list1)
# print(list_even)

#filter function
def even(n):
    return n%2==0
list_even=list(filter(even,list1))
print(list1,list_even)
list_even=list(filter(lambda x:x%2==0,list1))
list_odd=list(filter(lambda x:x%2!=0,list1))
print(list1)
print(list_even)
print(list_odd)

list_even2=list(map(lambda x: x*2,list_even))
print(list_even2)
sum=reduce(lambda x,y : x+y,list_even2)
print(sum)