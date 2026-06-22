print("Welcome to Mad Libs")
while True:
    name=input("Enter name")
    place=input("Enter place")
    animal=input("Enter animal")
    food=input("Enter food")
    verb=input("Enter verb in ing form")
    choice=int(input("Enter choice 1/2"))
    if choice==1:
        print(f"One day, {name} went to {place} carrying a {food}. Suddenly, a {animal} appeared and started {verb}. {name} was so surprised that he/she dropped the {food} and ran away!")
    elif choice==2:
        print(f"While eating a {food} in {place}, {name} saw a giant {animal}. The {animal} began {verb} in the middle of the road. Everyone started laughing, and {name} took a picture of it.")
    else:
        print("Sorry! Try again.")
    select=input("Try again? (y/n)").lower()
    if select=="n":
        break
