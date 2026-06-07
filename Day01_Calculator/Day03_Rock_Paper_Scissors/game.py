import random
choices=["rock","paper","scissors"]
while True:
    user_choice=input("play! rock,paper,scissors - shoot! or quit to stop playing").lower().strip()
    if user_choice=="quit":
        print("Thanks for playing!")
        break
    if user_choice not in choices:
        print("Invalid choice! Please type rock, paper, or scissors.")
        continue
    computer_choice=random.choice(choices)
    if computer_choice=="rock" and user_choice=="scissors":
        print("sorry, you lose!")
    elif computer_choice=="rock" and user_choice=="paper":
        print("yay, you win!")
    elif computer_choice=="paper" and user_choice=="rock":
        print("sorry, you lose!")
    elif computer_choice=="paper" and user_choice=="scissors":
        print("yay, you win!")
    elif computer_choice=="scissors" and user_choice=="paper":
        print("sorry, you lose!")
    elif computer_choice=="scissors" and user_choice=="rock":
        print("yay, you win!")
    elif computer_choice==user_choice:
        print("try again!")
