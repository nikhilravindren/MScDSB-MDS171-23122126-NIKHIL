#creating class called petstore and define functions collect,search,sell,listpets.
class petstore:
    def __init__(self):
        self.pet ={"dog":[],"cat":[],"rabbit":[],"parrot":[]}

    def collectpet(self,name,age,breed,price):
        details = {"age":age,"breed":breed,"price":price,"status":"available"}
        self.pet[name].append(details)
        print("pet added")
    def searchpet(self,name):
        for i in self.pet.keys():
            if i==name:
                print(self.pet[name])
                break
        breed = input("enter the breed:").lower()
        for i in self.pet[name]:
            if i["breed"]==breed:
                print(i)

    def sellpet(self,name,itemno):
        self.pet[name][itemno-1]["status"] = "sold"
        print("item sold")
    def listpet(self):
        print("available dogs are:")
        print(self.pet["dog"])
        print("available cats are:")
        print(self.pet["cat"])
        print("available rabbit are:")
        print(self.pet["rabbit"])
        print("available parrots are:")
        print(self.pet["parrot"])

            