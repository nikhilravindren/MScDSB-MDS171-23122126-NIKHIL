'''class MSCDSB:
    def __init__(self):
        self.name = "msc ds b"
        self.students =["a","b","c"]
    def printstudents(self):
        for student in self.students:
            print(student)

obj =MSCDSB()
print(obj.name)
print(obj.students)
obj.printstudents()'''

class car:
    def __init__(self,mgf,mdl,year):
        self.manufacturer = mgf
        self.model =mdl
        self.year = year
    def __str__(self):
        return self.manufacturer
mgf =(input("enter the manufacturer:"))
mdl =(input("enter the model name:"))
year =(input("enter the year:"))
bmw =car(mgf,mdl,year)
print(bmw.manufacturer)
print(bmw.model)
print(bmw.year)

