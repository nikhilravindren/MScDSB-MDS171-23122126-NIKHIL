listnames = []

def storename(name):
    name =name.strip().title()
    if name in listnames:
        return False
    else:
        listnames.append(name)
        return True

def printnames(name):
    print("-"*30)
    for name in listnames:
        print(name)
    print("-"*30)

def searchname(name):
    name= name.strip().title()
    flag = False
    for i in listnames:
        if name ==i:
            flag = True
            break
    if flag ==True:
        print("name exist")
    else:
        print("not found")

while True:
    print("manu options")
    print("*"*30)
    print("1.enter name")
    print("2.search name")
    print("3.list all names")
    print("4.exit")

    choice = int(input("enter choice"))

    if choice == 1:
       userinp = input("enter a name")
       retval = storename(userinp)
       if retval == True:
          print("name added")
       else:
           print("name exist")
    elif choice == 2:
        userinp = input("enter name")
        searchname(userinp)
    elif choice == 3:
       printnames()
    elif choice == 4:
       exit()
    else:
        print("invalid option")


