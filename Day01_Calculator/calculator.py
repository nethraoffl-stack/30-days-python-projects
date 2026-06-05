while True:
    n1=float(input("Enter first number"))
    n2=float(input("Enter second number"))
    operation=input("Enter operation (+, -, *, /)")
    if operation=="+":
        result=n1+n2
        print(result)
    elif operation=="-":
        result=n1-n2
        print(result)
    elif operation=="*":
        result=n1*n2
        print(result)
    elif operation=="/":
        try:
            result=n1/n2
            print(result)
        except ZeroDivisionError:
            print("Cannot divide by zero!")
    else:
        print("Operation invalid")
