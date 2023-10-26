class student:
    def __init__(self):
        self.list1={}

    def adding(self,name,rollno,state,course,mark):
        tem ={"rollno":rollno,"state":state,"course":course,"mark":mark}
        self.list1[name]=tem
        print("added succsesfully")
    def editting(self,name,change,value1):
        self.list1[name][change]=value1
        print("edited succsesfully")
    def search(self,name):
        value=False
        for key in self.list1.keys():
            if key==name:
                value=True
                break
        if value==True:
            print(name,"-",self.list1[name])
        elif value==False:
            print("name not found")
    def delete(self,name):
        value=False
        for key in self.list1.keys():
            print(key)
            if key==name:
                value=True
                break
        if value==True:
            del self.list1[name]
        else:
            print("name not found")
    def printing(self):
        print(self.list1)
def collect():
    name=input("enter your name").strip()
    rollno=input("enter rollnumber").strip()
    state=input("enter the state").strip()
    course=input("enter the course").strip()
    mark=input("enter the mark").strip()
    return name,rollno,state,course,mark
mystudent = student()
while True:
    print("welcome to mystudent portal")
    print("*"*30)
    print("press 1 for admin panal")
    print("press 2 for student access")
    user=int(input("who are you!"))
    if user==1:
        while True:
            print("welcome to mystudent portal")
            print("*"*30)
            print("press 1 for adding student details")
            print("press 2 for editing student details")
            print("press 3 for search for a student")
            print("press 4 for delete a student")
            print("press 5 for print all students")
            print("press 6 for exit")
            print("*"*30)

            choice =int(input("enter your choice"))

            if choice==1:
                name,rollno,state,course,mark=collect()
                mystudent.adding(name,rollno,state,course,mark)
            elif choice==2:
                name=input("enter the name that you want to make change:").strip()
                column=input("which section do you want to change:").strip()
                value1 =input("enter your new value:").strip()
                mystudent.editting(name,column,value1)
            elif choice==3:
                name=input("enter the name:").strip()
                mystudent.search(name)
            elif choice==4:
                name=input("enter the name:").strip()
                mystudent.delete(name)
            elif choice==5:
                mystudent.printing()
            elif choice==6:
                exit()
            else:
                print("choose currect option")

    elif user==2:
        while True:
            print("you can search your details here!")
            print("press 1 for search your details")
            print("press 2 for exit")
            choice =int(input("enter your choice"))
            if choice==1:
                name = input("enter your name").strip()
                mystudent.search(name)
            elif choice==2:
                exit()
            else:
                print("choose currect option")
    else:
        print("choose currect option")
                              

