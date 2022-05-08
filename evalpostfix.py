print("Python program to evaluate postfix expression: ")


def postfix_evaluate(ev,a):
    flag=0
    for i in ev:
        if(i.isdigit()):
            stk.append(i)
        else:
            
            if(a=='int' and flag==0):
                op2=int(stk.pop())
                op1=int(stk.pop())
            else:
                op2=float(stk.pop())
                op1=float(stk.pop())
            if(i== '+'):
                stk.append(op1+op2)
            elif(i== '-'):
                stk.append(op1-op2)
            elif(i== '*'):
                stk.append(op1*op2)  
            elif(i== '/'):
                if(op1%op2!=0):
                    flag=1
                stk.append(op1/op2)
            elif(i== '^'):
                stk.append(pow(op1,op2))
    return stk.pop()


stk=[]
postfix=["5","7","3","/","+"]

a=input("int or float: ")
ans=postfix_evaluate(postfix,a)
print(ans)