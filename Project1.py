#----------------------------------------------------------------------------------------
#Dice rolling simulator project
import random
from random import randrange

def dice():
    counter=0
    while counter<6:
        x=input("enter \'ok\' to continue or \'exit\' to stop rolling:")
        if x=="ok":
            num = random.randint(0, 6)
            #num=random.sample(range(7), 6)
            counter+=1
            print("the random number is:",num)
        elif x=="exit":
            break
        else:
            print("the input is invalid","please enter either ok or exit...")
#----------------------------------------------------------------------------------------
#calling dice function:
dice()