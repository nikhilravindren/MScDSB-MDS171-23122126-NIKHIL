import mymodule
mystore = mymodule.petstore()
while True:
    print("WELCOME TO CUTE PET")
    print("*"*30)
    print("press 1 for adding new pet")
    print("press 2 for search for a pet")
    print("press 3 for sell a pet")
    print("press 4 for list all the pet ")
    print("press 5 for exit")
    choice = int(input("enter your choice"))

    if choice == 1:
        name = input("enter the pet name:")
        age = input("enter the age of the pet:")
        color = input("enter the color:")
        price =input("enter the price:")
        mystore.storing(name,color,age,price)
    elif choice == 2:
        name = input('enter the name of the pet:')
        mystore.search(name)
    elif choice == 3:
        name =input("enter the name of the pet:")
        mystore.sellpet(name)
    elif choice == 4:
        mystore.listpets()
    elif choice == 5:
        exit()
    else:
        print("you enterd a wrong number")

                                                                                                                                                                                                                                                                                                                                                    
