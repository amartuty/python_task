print(" Welcome to Gaming world")

import random
   
choice1=["rock","paper","scissor"]

computer= random.choice(choice1)

computer_score = 0
gamer_score = 0
ties=0


while True:
    gamer=input("rock, paper or  scissor: ")
    if gamer==computer:
        print("Both selection are same so its a TIE")
    elif gamer=="rock":
        if computer=="paper":
            print("you lose")
            computer_score+=1
        else:
            print("You win!")
            gamer_score+=1
    elif gamer=="paper":
        if computer =="scissor":
            print("You lose!")
            computer_score+=1
        else:
            print("You win!")
            gamer_score+=1
    elif gamer == "scissor":
        if computer == "rock":
            print("You lose...")
            computer_score+=1
        else:
            print("You win!")
            gamer_score+=1
    elif gamer=='end':
        print("Final Scores:")
        print(f"computer:{computer_score}")
        print(f"gamer:{gamer_score}")
        break
        
