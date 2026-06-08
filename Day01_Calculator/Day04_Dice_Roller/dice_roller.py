import random
while True:
    choice=input("Want to play dice? Click y to play or q to quit").lower()
    if choice=="q":
        print("Thanks for playing!")
        break
    else:
        dice=random.randint(1,6)
        print("Your dice number is",dice)
