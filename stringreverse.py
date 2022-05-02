str1=input("enter first string")
l=len(str1)
s=""
for i in range(l-1,-1,-1):
    s+=str1[i]
print("the reverse string is ",s)