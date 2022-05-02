# program for details of one student
print("student's details")
a=["AKHIL","indore","akhil@gmail.com",443356]
a.append("IT-2K20-04")
print("NAME :",a[0])
print("address :",a[1])
print("email :",a[2])
print("mobno :",a[3])
print("rollno :",a[4])
for i in a:
    print(i)
x=a.index(443356)
print(x)