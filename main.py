'''
1 for snake
-1 for water
0 for gun
'''
import random

computer = random.choice([-1,0,1])
yourStr = input("Enter your choice: ")
yourDict = {"s": 1,"w": -1,"g": 0}
reverseDict = {1:"Snake",-1:"Water",0:"Gun"}


you = yourDict[yourStr]
#By now we have two number (veriables),you and computer

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if computer==you:
    print("Draw")

else:
        if(computer==-1 and you==1):
            print("You win!")
        elif(computer==-1 and you==0):
            print("you lose!")
        elif(computer==1 and you==-1):
            print("You win")
        elif(computer==0 and you==-1):
            print("You win!")
        elif(computer==0 and you==1):
            print("You lose!")
        elif(computer==1 and you ==0):
            print("You win!")