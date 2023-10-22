def input_num():
    x = int(input("Enter First Number of your choice: "))
    y = int(input("Enter Second Number of your choice: "))
    return x,y
def add(x,y):
    print(f"Result: {x+y}")
def subtract(x,y):
    print(f"Result: {x-y}")
def multiply(x,y):
    print(f"Result: {x*y}")
def division(x,y):
    if y!=0:
        print(f"Result: {x/y}")
    else:
        print("Denominator can't be Zero")

def welcome_msg():  
    print("""
        PRESS 1 FOR ADDITION
        PRESS 2 FOR SUBTRACTION
        PRESS 3 FOR MULTIPLICATION
        PRESS 4 FOR DIVISION
        PRESS 5 FOR EXIT""")
print("<---CALCULATOR WITH BASIC ARITHMETIC OPERATIONS--->")
while(True):
    welcome_msg()
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        x,y = input_num()
        add(x,y)
    elif choice==2:
        x,y = input_num()
        subtract(x,y)
    elif choice ==3:
        x,y = input_num()
        multiply(x,y)
    elif choice ==4:
        x,y = input_num()
        division(x,y)
    elif choice ==5:
        exit()
    else :
        print("Enter Correct Choice")   