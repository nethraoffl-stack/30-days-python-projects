while True:
    print("==Temperature Converter==")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")
    choice=int(input("Enter your choice(1/2/3)"))
    if choice==1:
        Celsius=float(input("Enter Celsius"))
        Fahrenheit=(Celsius * 9/5) + 32
        print(Fahrenheit)
    elif choice==2:
        Fahrenheit=float(input("Enter Fahrenheit"))
        Celsius=(Fahrenheit - 32)/1.8
        print(Celsius)
    else:
        break
