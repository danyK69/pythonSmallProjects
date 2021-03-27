import math

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def mutiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def sqrt(a):
    result=math.sqrt(a)
    return result

def exp(a):
    return a ** 2

def sin(a):
    result=math.sin(a)
    return result

def cos(a):
    result=math.cos(a)
    return result

def tan(a):
    result=math.tan(a)
    return result

#selecting operations

print('''
Select the  number for the required operation:

1 - Addition(x,y)
2 - Subtraction(x,y)
3 - Multiplication(x,y)
4 - Division(x,y)
5 - Square(x)
6 - Square root(x)
7 - Sin(x)
8 - Cos(x)
9 - Tan(x) ''')

op=int(input("What do you want to perform: "))

while op<10:
    if op==1:
        print("Enter the parameters: ")
        x1 = int(Input("Enter 1st number: "))
        y1 = int(Input("Enter 2nd number: "))
        res1=add(x1,y1)
        print("Addition= ",res1)

    elif op==2:
        print("Enter the parameters: ")
        x2 = int(Input("Enter 1st number: "))
        y2 = int(Input("Enter 2nd number: "))
        res2=subtract(x2,y2)
        print("Subtraction= ",res2)

    elif op == 3:
        print("Enter the parameters: ")
        x3 = int(Input("Enter 1st number: "))
        y3 = int(Input("Enter 2nd number: "))
        res3 = multiply(x3, y3)
        print("Product of the two numbers = ", res3)

    elif op == 4:
        print("Enter the parameters: ")
        x4 = int(Input("Enter 1st number: "))
        y4 = int(Input("Enter 2nd number: "))
        res4 = divide(x4, y4)
        print("Division of the 2 numbers = ", res4)

    elif op==5:
        x5 =int(input("Enter a number: "))
        res5=exp(x5)
        print("Square= ",res5)

    elif op == 6:
        x6 = int(input("Enter a number: "))
        res6 = sqrt(x6)
        print("Square root= ", res6)

    elif op == 7:
        x7 = int(input("Enter a number: "))
        res7 = sin(x7)
        print("Sin(",x7,") = ", res7)

    elif op == 8:
        x8 = int(input("Enter a number: "))
        res8 = cos(x8)
        print("Cos(x)= ", res8)

    elif op == 9:
        x9 = int(input("Enter a number: "))
        res9 = exp(x9)
        print("Tan(x)= ", res9)

    else:
        print("\nChoose another operation")

    new = int(input("Do you want to continue - ( yes - 1)/( no - 0) : "))
    if new==1:
        op=int( input("Enter another operation: "))
    elif new == 0:
        print("\nThank  you for using the scientific calculator")
        break











