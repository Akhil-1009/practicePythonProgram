f=open("myfirst_file.txt ","w")
x="jai shree ram"
y="akhil"

# file write operation
f.write(x)
f.write("\n")
f.write(y)
f.close()
#file read operation

f=open("myfirst_file.txt","r")
z=f.read()
print(z)
f.close()