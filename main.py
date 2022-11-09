# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#/* This is going to be a basic calculator for my first project*/

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y

while True:
    oper = input("Enter operation (1 =add |2 =subtract | 3 =multiply | 4 =divide): ")
    if oper in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    if oper == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif oper == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif oper == '3':
        print(num1, "*", num2, "=", multiplication(num1, num2))

    elif oper == '4':
        print(num1, "/", num2, "=", division(num1, num2))

    # check if user wants another calculation
    # break the while loop if answer is no
    next_calculation = input("Press 'Enter' to continue using the calculator press 'q' to quit: ")
    if next_calculation == "q":
        break
    else:
        print('')







