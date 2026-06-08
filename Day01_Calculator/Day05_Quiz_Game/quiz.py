print("Welcome to the quiz")
count=0
while True:
    choice=input("click y to continue or q to quit")
    if choice=="q":
        print("Thanks for playing!")
        break
    else:
        answer1=input("What is the capital of India?").lower()
        if answer1=="delhi":
            print("yay! correct")
            count+=1
        else:
            print("Oops! wrong")
        answer2=int(input("What is 5 + 7?"))
        if answer2==12:
            print("yay! correct")
            count+=1
        else:
            print("Oops! wrong")
        print("Final score is",count)
        break        
