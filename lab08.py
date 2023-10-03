class stack:
    def __init__(self):
        self.slist = []
    def push_item(self,item):
        self.slist.append(item)
        print("item added")
    def pop_item(self):
        self.slist.pop()
        print("item removed")
    def print_item(self):
        print("your stack is:{}".format(self.slist))
    def stack_size(self):
        print("your stack condains {} elements".format(len(self.slist)))
    def top_item(self):
        print("last element is:",self.slist[len(self.slist)-1])
    def check_empty(self):
        if len(self.slist) == 0:
            print("the stack is empty")
        else:
            print("stack is not empty")
my_stack = stack()
while True:
    print("press 1 for push item into stack")
    print("press 2 for pop item from the stack")
    print("press 3 for print items in the stack")
    print("press 4 for size of the stack")
    print("press 5 for finding the top item")
    print("press 6 for checking the stack empty or not")
    print("press 7 for exit the program")
    choice = int(input("enter your choice:"))
    if choice ==1:
        item = input("enter the item:")
        my_stack.push_item(item)
    elif choice ==2:
        my_stack.pop_item()
    elif choice ==3:
        my_stack.print_item()
    elif choice ==4:
        my_stack.stack_size()
    elif choice ==5:
        my_stack.top_item()
    elif choice ==6:
        my_stack.check_empty()
    elif choice ==7:
        exit()
    else:
        print("choose currect option")