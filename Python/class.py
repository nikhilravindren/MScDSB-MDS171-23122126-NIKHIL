
def save_details(name,age,gender):
    with open("christ.csv","a+") as file:
        file.write(name+",")
        file.write(str(age)+",")
        file.write(gender+"\n")
        file.close()

def check_details():
    name = input("enter your name:").strip()
    file =open("christ.csv")
    lines =file.readlines()
    for line in lines:
        tem = line.split(",")        
        i = tem[0]
        value = False
        if i == name:
            value = True
            break
    if value == True:
        print("name found")
    else:
        print("name not found")
def print_details():
    name = input("enter name: ").strip()
    file =open("christ.csv")
    lines =file.readlines()
    for line in lines:
        tem = line.split(",")
        i = tem[0]
        if i ==name:
            print(tem[0],"\n",tem[1],"\n",tem[2])

def take_input():
    name = input("enter your name: ").strip()
    age = input("enter your age: ").strip()
    gender = input("enter your gender:").strip()
    return name,age,gender

while True:
    print("your menu")
    print("*"*30)
    print("type 1 for save details to file")
    print("type 2 for check your name")
    print("type 3 for show your details")
    print("type 4 for exit")

    choice = int(input("enter your choice:"))

    if choice == 1:
        name,age,gender = take_input()
        save_details(name,age,gender)
        print("saved successfully")
    elif choice == 2:
        check_details()
    elif choice == 3:
        print_details()
    elif choice == 4:
        exit()
    else:
        print("choose correct option")






        