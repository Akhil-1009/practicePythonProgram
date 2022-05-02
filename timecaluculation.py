import time
# a=int(input("enter a number for factorial"))
def facto(no):
    fact=1
    for i in range(1,no+1):
        fact=fact*i
    return fact
def facto1(n):
    if(n==0 or n==1):
        return 1
    return n*(facto1(n-1))
f=open("my_file_txt2","w")
f.write(" ")
f.close()
for i in range(5,20):
    initial=time.time()
    fact1=facto(i)
    print(fact1,"\n")
    t1=time.time()-initial
    fact2=facto1(i)
    print(fact2)
    t2=time.time()-t1
    f=open("my_file_txt2","a")
    t1=str(t1)
    t2=str(t2)
    f.write(t1)
    f.write("\t")
    f.write(t2)
    f.write("\n")
    f.close()
f=open("my_file_txt2","r")
d=f.read()
f.close()
l=[]
l=d.split("\n")
print("data is:",l)

