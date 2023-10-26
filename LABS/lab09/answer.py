#importing the file then call the class in loop we creating menu
import module
myshop =module.petstore()
while True:
    print("WELCOME TO MYSHOP")
    print("*"*30)
    print("press 1 for adding the pet")
    print("press 2 for search for pet")
    print("press 3 for selling the pet")
    print("press 4 for getting all the pets")
    print("press 5 for exit")

    choice = int(input("enter your choice"))

    if choice == 1:
        name =input("enter the name:").lower()
        age = input("enter the age:")
        breed =input("enter the breed:")
        price = input("enter the price:")
        myshop.collectpet(name,age,breed,price)
    elif choice == 2:
        print("we have 4 Type of pet given below select from it")
        print("dog,cat,parrot,rabbit")
        name = input("enter the name:")
        myshop.searchpet(name)
    elif choice == 3:
        name =input("enter the name:")
        myshop.searchpet(name)
        itemno = int(input("enter the item number:"))
        myshop.sellpet(name,itemno)
    elif choice == 4:
        myshop.listpet()
    elif choice == 5:
        exit()
    else:
        print("choose currect option")


