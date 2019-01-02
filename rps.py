## A game rock paper scissor


### Rules
# 1. Rock > Scissors
# 2. Scissors > paper
# 3. Paper > Rock
###

import random

while True:
    print ("Which option do you prefer Rock / Paper or Scissors")
    a = input("Player 1 input:")

    if a in ('rock','paper','scissors'):
        print ("Player1 selection is:",a)
        break
    else:
        print ("Please enter proper input")

ran = ['rock','paper','scissors']
def list_random(ran):
    random.shuffle(ran)
    return ran[0]
    
player2 = list_random(ran)
print ("Player2 selection is:",player2)

 
if a in ('rock') and player2 in ('scissors'):
    print ("Player1 wins")
elif a in ('rock') and player2 in ('paper'):
    print ('Player2 wins')
elif a in ('paper') and player2 in ('scissors'):
    print ("Player2 wins")
elif a in ('paper') and player2 in ('rock'):
    print ("Player1 wins")
elif a in ('scissors') and player2 in ('rock'):
    print ("Player2 wins")
elif a in ('scissors') and player2 in ('paper'):
    print ("Player1 wins")
else:
    print ("TIE")    