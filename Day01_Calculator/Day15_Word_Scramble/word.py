import random
while True:
    print("Welcome to word scramble")
    llist=["python","computer","electronics","current","keyboard","electrons"]
    choice=random.choice(llist)
    letters=list(choice)
    random.shuffle(letters)
    word=" ".join(letters)
    print("Here's your scrambled word",word)
    user=input("Enter your guess")
    if user==choice:
        print("Yay! You got it!")
    else:
        ch=input("Try again?")
        if ch=="n":
            break
