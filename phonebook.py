class contact:
    def __init__(self,contact_number,f_name):
        self.contact_number=contact_number
        self.f_name=f_name
    def putdata(self):
        f=open("phonebookfile.txt","a")
        f.write(self.contact_number)
        f.write("\t")
        f.write(self.f_name)
        f.write("\n")
        f.close()
    def getdata():
        f=open("phonebookfile.txt","r")
        i=f.read()
        f.close()
        return i
# contact_name=input("enter the contact name")
# contact_number=input("enter the contact number")
#  contact1=contact(contact_number,contact_name)
# contact1.putdata()
result=contact.getdata()
list1=[]
list1=result.split("\n")
list2=[]
for i in list1:
    list2.append(i.split("\t"))
print("the records are",list1)
print("the new records are ",list2)
len1=len(list2)
for i in range(0,len1-1):
     for j in range(0,2):
         print(list2[i][j],end="\t")
     print("\n")
    