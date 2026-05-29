# This is a one round game like 'Stone Paper Scissor'

import sys
import random
print("WELCOME TO 'SNAKE-WATER-GUN' GAME")

user = int(input("Enter '0' for Snake \nEnter '1' for Water \nEnter '2' for Gun   : "))

Option = [0 , 1 , 2]
comp = random.choice(Option)
print("The Computer Chosses: ",comp)

if(user > 2):
    print("invalid input \n GAME ENDED")
    sys.exit()

def check(comp , user):
    if(comp == user):
        return "and the computer has same IQ so its a DRAW"
    
    if(comp == 0 and user == 1):
        return "Lose"
    
    if(comp == 1 and user == 2):
        return "Lose"
    
    if(comp == 2 and user == 0):
        return "Lose"
    
    return "Win"

print("You",check(comp , user))