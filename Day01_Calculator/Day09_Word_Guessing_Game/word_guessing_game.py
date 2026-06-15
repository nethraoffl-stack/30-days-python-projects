print("Welcome to Hangman!")
lst=["Computer","Python","Java","Keyboard"]
choice=int(input("Enter a random number from 1-4"))
print("Ok! Word chosen.")
if choice==1:
    print("C_mpu_er")
    userinput=input("Enter word you guessed?")
    if userinput=="Computer":
        print("Yay! You guessed it right!!")
    else:
        print("Sorry! You're wrong!!")
elif choice==2:
    print("P_t_on")
    userinput=input("Enter word you guessed?")
    if userinput=="Python":
        print("Yay! You guessed it right!!")
    else:
        print("Sorry! You're wrong!!")
elif choice==3:
    print("J_v_")
    userinput=input("Enter word you guessed?")
    if userinput=="Java":
        print("Yay! You guessed it right!!")
    else:
        print("Sorry! You're wrong!!")
elif choice==4:
    print("K_y_oa_d")
    userinput=input("Enter word you guessed?")
    if userinput=="Keyboard":
        print("Yay! You guessed it right!!")
    else:
        print("Sorry! You're wrong!!")
    

