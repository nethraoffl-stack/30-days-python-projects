def write():
    while True:
        f=open("Journal.txt","a")
        line=input("Write your entry")
        f.write(line+"\n")
        choice=input("Add more?").lower()
        f.close()
        if choice=="n":
            break
def read():
    f=open("Journal.txt","r")
    lines=f.readlines()
    for line in lines:
        print(line)
    f.close()
print("Welcome to your journal!")
print("1. Write Entry 2. View Entries 3. Exit")
while True:
    user=int(input("Enter your choice"))
    if user==1:
        write()
    elif user==2:
        read()
    elif user==3:
        print("Thanks for using!")
        break
