parking_lot=[1203,3402,4568,8904,8765,4576,2345,9021]
while True:
    print("Welcome to parking lot")
    print("1.Park a vehicle 2.Remove a vehicle 3.View available parking spaces 4.Exit")
    choice=input("Enter choice")
    if choice=="Park a vehicle":
        if len(parking_lot)<20:
            car=int(input("Enter your 4 digit car number"))
            parking_lot.append(car)
        else:
            print("Parking lot is full!")
    elif choice=="Remove a vehicle":
        car=int(input("Enter your 4 digit car number"))
        if car in parking_lot:
            parking_lot.remove(car)
        else:
            print("Your vehicle is not parked")
    elif choice=="View available parking spaces":
        print(20 - len(parking_lot))
    elif choice=="Exit":
        print("Thanks for using!")
        break
