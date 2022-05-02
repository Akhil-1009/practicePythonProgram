from ast import operator

def convert(infix):
    stk=[]
    top=-1
    post=[]
    prior={"+":1,"-":1,"*":2,"/":2,"^":3}
    for i in infix:
        if(i.isdigit()):
            post.append(i)
        elif(i=="("):
            stk.append(i)
            top=top+1
        elif(i==")"):
            while(stk[top]!="(" or top==-1):
                post.append(stk.pop())
                top=top-1
            stk.pop()
            top=top-1    
        else:
            if(top==-1):
                stk.append(i)
                top=top+1
            elif(stk[top]=='('):
                stk.append(i)
                top=top+1
            elif(prior.get(stk[top])>=prior.get(i)):
                while((top!=-1) and prior.get(i)>prior.get(stk[top])):
                    post.append(stk.pop())
                    top=top-1
                stk.append(i)
                top=top+1
            else:
                stk.append(i)
                top=top+1
    while(top!=-1):
        post.append(stk.pop())
        top=top-1
    print(post)            
print("INFIX TO POSTFIX")
operator=["+","-","/","*","%","(",")"]
numeral=["0","1","2","3","4","5","6","7","8","9","."]
expression=[]
input_exp=input("enter the expression")
print("input =",input_exp)
operand=""
flag=0
for i in input_exp:
    if i in numeral:
        operand=operand+i
        flag=1
    elif i in operator:
        if(flag==1):
            expression.append(operand)
            operand=""
            flag=0
            expression.append(i)
        else:
            expression.append(i)
    else:
        print("invalid expression")
        break
if(flag==1):
    expression.append(operand)
print("input in list =",expression)
convert(expression)