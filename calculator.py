# Modulo function defination
from pickle import TRUE


def mod(x,y):
	z=x%y
	return z
def add(x,y):
    z=x+y
    return z
def sub(x,y):
    z=x-y
    return z
def mul(x,y):
    z=x*y
    return z
def div(x,y):
    z=x//y
    return z
def square(x):
	if(x==0):
		return 1
	else:
		return x**x
def power(x,y):
	if(y==0):
		return 1
	else:
		return x**y
def root(x):
	return power(x,0.5)
def cuberoot(x):
	return power(x,1/3)

#function to check string or number and typecasting the number
def check(temp,a):
	l=len(temp)
	for i in range(0,l):
		if(temp[i]=='0' or temp[i]=='1' or temp[i]=='2'  or temp[i]=='3' or temp[i]=='4' or temp[i]=='5' or temp[i]=='6' or temp[i]=='7' or temp[i]=='8' or temp[i]=='9' or temp[i]=='.'):
			#print("Anshul")
			if(temp[i]==temp[l-1]):
				if(a=='int'):
					temp=int(temp)
					return temp
				elif(a=='float'):
					temp=float(temp)
					return temp
				else:
					print("Invalid input string.")
					exit()
		else:
			print("You may input string , string never perform arithmetic opration.")
			exit()


#Starting of program
print("Welcome To Akhil's Calculator")

def binary(a):

	x=input("Enter first value: ")
	y=input("Enter second value: ")
	x=check(x,a)
	y=check(y,a)
	return (x,y)
def unary(a):
	x=input("enter the value")
	x=check(x,a)
	return x
while TRUE:
	a=str.lower(input("Enter which type of value(int,float) u want to enter: "))
	print("'+' for addition\n'-' for substraction\n'*' for multiplication\n'/' for division\n'%' for modulo. \n'sq' for square.\n 'sqroot' for root.\n '^' for power.\n cubroot for cuberoot ")
	op=input("Enter any above operator to perform opration: ")

	if(op=='+'):
		x,y=binary(a)
		i=add(x,y)
		print(x,"+",y,"=",i)
	elif(op=='-'):
		x,y=binary(a)
		i=sub(x,y)
		print(x,"-",y,"=",i)
	elif(op=='*'):
		x,y=binary(a)
		i=mul(x,y)
		print(x,"*",y,"=",i)
	elif(op=='/'):
		x,y=binary(a)
		if(y==0):
			print("Division by 0 is not allowed.")
		else:
			i=div(x,y)
			print(x,"/",y,"=",i)
	elif(op=='%'):
		x,y=binary(a)
		if(y==0):
			print("Division by 0 is not allowed.")
		else:
			i=mod(x,y)
			print(x,"%",y,"=",i)
	elif(op=='sq'):
		x=unary(a)
		result=square(x)
		print(x,"square = ",result)
	elif(op=="^"):
		x,y=binary(a)
		result=power(x,y)
		print(x,"^",y,result)
	elif(op=="sqroot"):
		x=unary(a)
		result=root(x)
		print(x,"root =",result)
	elif(op=="cubroot"):
		x=unary(a)
		result=cuberoot(x)
		print(x,"cube root =",result)
	else:
		print("Invalid oprator")
	choice=input("do you want to continue press y for yes n for no")
	if(choice=="n"):
		break