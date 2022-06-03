print("Welcome to Calculator")

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
op = input("\nEnter the operation you want to perform\n+ for Add\n- for Subtract\n* for Multiply\n/ for Divide\nEnter operator : ")

if(op == '+'):
    print("Sum = "+str(add(x,y)))
elif(op == '-'):
    print("Difference = "+str(subtract(x,y)))
elif(op == '*'):
    print("Product = "+str(multiply(x,y)))
elif(op == '/'):
    print("Quotient = "+str(divide(x,y)))
else:
    print("Invalid operator")