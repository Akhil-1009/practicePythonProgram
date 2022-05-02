count1=0
count2=0
import random
for i in range(0,6):
    user1=int(input("please enter your move 1 for rock 2 for paper and 3 for scissor "))
    computer=random.randint(1,3)

    if((user1==1) and (computer==3)):
        print("user1 is winner")
        count1=count1+1
    elif((user1==2)and (computer==1)):
        print("user 1 is winner")
        count1=count1+1
    elif((user1==3)and (computer==2)):
        print("user1 is winner")
        count1=count1+1
    elif((computer==1) and (user1==3)):
        print("computer is winner")
        count2=count2+1
    elif((computer==2)and (user1==1)):
        print("user 2 is winner")
        count2=count2+1
    elif((computer==3)and (user1==2)):
        print("computer is winner")
        count2=count2+1
    else:
        print("draw")
if(count1>count2):
    print("the winner of the match is user1")
elif(count2>count1):
    print("the winner of the match is computer")
else:
    print("the result is draw")