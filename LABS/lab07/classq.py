#create a class resturant,that accepts item name,qty as input
#inside the class your having the item
#and its cost as a dictionary 
#create a funtion calculate total cost
#that print the item name,qty,total cast
# class resturant:
#     def __init__(self,itemname,qty):
#         self.itemname = itemname
#         self.qty = qty
#         self.menuitems = {
#             "rice":30,
#             "chiken":100,
#             "dal":40,
#             "chapathi":15
#         }
#     def totalcost(self):
#         print("item :",self.itemname)
#         print("quantity :",self.qty)
#         print("total :",self.qty*self.menuitems[self.itemname])
# itemname =input("enter the item:")
# qty =int(input("enter the quantity:"))
# order = resturant(itemname,qty)
# order.totalcost()
#define a class expense tracker that store the expenses and income in a dict
#implement the method to to store the transaction
#calculate the total expense/income
class expensetracker:
    def __init__(self):
        self.store ={
            "income":[],
            "expense":[]
        }
    def storetransation(self,type1,amt,category,date,details):
        trans = {
            "amount":amt,
            "category":category,
            "date":date,
            "details":details
        }
        if type1 =="income":
            self.store["income"].append(trans)
        elif type1 == "expense":
            self.store["expense"].append(trans)
    def totel(self):
        total_income =0
        for i in self.store["income"]:
            total_income += int(i["amount"])
        total_expense =0
        for i in self.store["expense"]:
            total_expense += int(i["amount"])
        print("income: {} and expense: {}".format(total_income,total_expense))

    def print_trans(self):
        print("your incomes:")
        for i in self.store["income"]:
            print(i)
        print("your expenses:")
        for i in self.store["expense"]:
            print(i)
    def addto_file(self):
        with open("expense.csv","a+") as file:
            file.write(str(type1)+","+str(amt)+","+str(category)+","+str(date)+","+str(details)+"\n")



def collectinfo():
    amt = input("enter amount:")
    category = input("enter category:")
    date = input("enter date:")
    details =input("enter details:")
    return amt,category,date,details

myexpense = expensetracker()

while True:
    print("....my expense tracker ....")
    print("1.store income")
    print("2.store expense")
    print("3.view transcation")
    print("4.total expense")
    print("5.save to file")
    print("6.exit")

    choice = int(input("enter your choice:").strip())
    if choice == 1:
        amt,category,date,details = collectinfo()
        type1 = "income"
        myexpense.storetransation(type1,amt,category,date,details)
    elif choice == 2:
        amt,category,date,details = collectinfo()
        type1 = "expense"
        myexpense.storetransation(type1,amt,category,date,details)
    elif choice == 3:
        myexpense.print_trans()
    elif choice == 4:
        myexpense.totel()
    elif choice == 5:
        myexpense.addto_file()
    elif choice == 6:
        exit()
    else:
        print("enter a valid choice")
    

