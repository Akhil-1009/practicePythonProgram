def avg(*value):
    x=0
    for i in value:
        x=x+i
    return x/len(value)
y=avg(3,4,5)
print(y)
print(avg(5,7,8,8,9,8))
