# n=int (input("enter a no") )
# print("table of ",n,"is")
# m=n*10
# p=1
# for i in range(n,m+1,n):
#     print(n,"*",int(i/n),"=",i)
n=int (input("enter a no") )
print("table of ",n,"is")
m=n*10
p=1
for i in range(n,m+1,n):
    print("{} * {}={}".format(n,p,i))
    p+=1