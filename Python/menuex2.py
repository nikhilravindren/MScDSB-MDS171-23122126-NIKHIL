
dict1 = {}
def storestudent(name,rgno,email,phone):
    student ={
        "Name":name,
        "email":email,
        "phone":phone
    }
    dict1[rgno] = student

def searchstudent(srgno,dict1):
    tem =False
    for rgno in dict1.keys():
        if rgno ==srgno:
            tem =True
    if tem ==True:
        print("student found")
    else:
        print("student not found")

def printstudent(prgno,dict1):
    for rgno in dict1.keys():
        if rgno == prgno:
            print(dict1[prgno])


while True:
    print("menu options")
    print("*"*30)
    print("type 1 for:create students")(
    print("type 2 for:search for students")
    print("type 3 for:print students")
    print("type 4 for:exit")

    choice = int(input("enter your choice:"))

    if choice == 1:
        rgno = input("enter registor no:")
        name = input("enter your name: ")
        email = input("enter your mail id:")
        phone =input("enter your number:")
        storestudent(name,rgno,email,phone)
        print("your details stored!")
    elif choice ==2:
        srgno =input("enter the registor number:")
        searchstudent(srgno,dict1)
    elif choice == 3:
        prgno = input("enter your registor number:")
        printstudent(prgno,dict1)
    elif choice == 4:
        exit()
    else:
        print("you choose a wrong option please enter the right one")