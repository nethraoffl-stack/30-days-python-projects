balance=20000
while True:
    print("Welcome to XYZ bank")
    print("1.View Balance 2.Deposit 3.Transaction 4.Exit")
    choice=input("Enter your choice : ")
    if choice=="View Balance":
        print("Your bank balance is",balance)
    elif choice=="Deposit":
        deposit=int(input("Enter your deposit"))
        balance+=deposit
    elif choice=="Transaction":
        transaction=int(input("Enter your transaction"))
        if transaction<balance or transaction==balance:
            balance-=transaction
        else:
            print("Sorry. Money not sufficient.")
    elif choice=="Exit":
        print("Thanks for using XYZ bank.")
        break
