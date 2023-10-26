class saving():
    def __init__(self):
        self.save = {}
    
    def storing(self,name,age,gender,rollno):
        details ={
            "name":name,
            "age":age,
            "gender":gender
            }
        self.save[rollno] =details
    
    def verified(self,rollno):
        a =self.save.keys()
        value = False
        for i in a:
            if i == rollno:
                value = True
        if value == True:
            print("your details are verified")
        else:
            print("fake roll number")
    def printing(self,rollno):
        a =self.save.keys()
        value = False
        for i in a:
            if i == rollno:
                value = True
        if value == True:
            print("roll number is {} and details are {}".format(rollno,self.save[rollno]))
        else:
            print("your details are not found")
my_details = saving()
while True:
    print("welcome to C school")
    print("*"*30)
    print("press 1 for storing your details")
    print("press 2 for verifing your details")
    print("press 3 for printing your details")
    print("press 4 for exiting")

    choice = int(input("enter your choice:"))

    if choice == 1:
        rollno = input("enter your roll number:")
        name = input("enter your name:")
        age = input("enter your age:")
        gender = input("enter your gender:")
        my_details.storing(name,age,gender,rollno)
    elif choice == 2:
        rollno = input("enter your roll number:")
        my_details.verified(rollno)
    elif choice == 3:
        rollno = input("enter your roll number:")
        my_details.printing(rollno)
    elif choice == 4:
        exit()
    else:
        print("choose currect option!")

        
                