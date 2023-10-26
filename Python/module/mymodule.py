# class student:
#     def __init__(self,name,phone):
#         self.name = name
#         self.phone = phone

#     def printstudent(self):
#         print(self.name,self.phone)

#create a petstore class where you have the details of pets available and their details.
#store new pet details,search for a pet,sell a pet,list all pets
#import this and create a petstoremain file, where you will implement a menu driven program for admin who will manage the store
#user who will see the pets and buy pets
class petstore:
    def __init__(self):
        self.stored = []

    def storing(self,name,color,age,price):
        store ={}
        details ={"color":color,
                  "age":age,
                  "price":price,
                  "status":"available"}
        store["name"] =name
        store["details"]=details
        self.stored.append(store)
        print("pet added ")
    def search(self,name):
        value = False 
        for p in self.stored:
            if p["name"] ==name:
                print(p)
                value = True
        if value ==False:
            print("no pet found")
        
            
            
    def sellpet(self,name):
        for i in self.stored:
            if i["name"]==name:
                i["details"]["status"]="sold"
                print("sold it")
                break
            else:
                print("no pet found")
    def listpets(self):
        print("available pets are:")
        for i in self.stored:
            print(i)
            


    
        