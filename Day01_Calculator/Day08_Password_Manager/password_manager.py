import csv
def add():
    f=open("Passwords.csv","a",newline="")
    writer=csv.writer(f)
    while True:
        Website=input("Enter website name")
        Password=input("Enter password")
        writer.writerow([Website,Password])
        ch=input("want to add more?")
        if ch=="n":
            break
    f.close()
def read_passwords():
    f=open("Passwords.csv","r",newline="")
    reader=csv.reader(f)
    for row in reader:
        print(row[1])
    f.close()
def search():
    f=open("Passwords.csv","r",newline="")
    reader=csv.reader(f)
    p=input("Enter website to search password")
    for row in reader:
        if row[0]==p:
            print(row[1])
    f.close()
print("Welcome to password manager")
while True:
    print("1. Add 2.View 3.Search 4.Exit")
    choice=int(input("Enter choice"))
    if choice==1:
        add()
    elif choice==2:
        read_passwords()
    elif choice==3:
        search()
    elif choice==4:
        break
