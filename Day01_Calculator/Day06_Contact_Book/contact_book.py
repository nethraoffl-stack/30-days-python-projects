import csv
import os

def create():
    has_file = os.path.exists("contacts.csv")    
    f=open("contacts.csv","a",newline="")
    writer=csv.writer(f)
    if not has_file:
        writer.writerow(["name","contact"])        
    while True:
            name=input("Enter name")
            contact=int(input("Enter 10 digit contact number"))
            writer.writerow([name,contact])
            user=input("add more?")
            if user=="n":
                break
    f.close()
def read():
    f=open("contacts.csv","r",newline="")
    reader=csv.reader(f)
    for row in reader:
        print(row)
    f.close()
def search():
    f=open("contacts.csv","r",newline="")
    sname=input("Enter name to search contact number")
    reader=csv.reader(f)
    flag=0
    for row in reader:
        if row[0]==sname:
            flag=1
            print(row)
    if flag==0:
        print("sorry, not found!")
    f.close()
def delete():
    f=open("contacts.csv","r",newline="")
    f1=open("Newcontacts.csv","w",newline="")
    sname=input("Enter name to delete contact number")
    reader=csv.reader(f)
    writer=csv.writer(f1)
    for row in reader:
        if row[0]==sname:
            print("Found!")
        else:
            writer.writerow(row)
    f.close()
    f1.close()
    os.remove("contacts.csv")
    os.rename("Newcontacts.csv", "contacts.csv")
while True:
    print("welcome to contact book!")
    print("1. Add 2.View 3.Search 4.Delete 5.Exit")
    choice=int(input("Enter your choice"))
    if choice==5:
        break
    elif choice==1:
        create()
    elif choice==2:
        read()
    elif choice==3:
        search()
    elif choice==4:
        delete()
