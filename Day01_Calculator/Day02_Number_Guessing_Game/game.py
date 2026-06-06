import random
number=random.randint(1,100)
while True:
    guess_number=int(input("Guess a number between 1 and 100: "))
    if guess_number>number:
        print("Too high!")
    elif guess_number<number:
        print("Too low!")
    elif guess_number==number:
        print("Congratulations! You guessed it!")
        break
