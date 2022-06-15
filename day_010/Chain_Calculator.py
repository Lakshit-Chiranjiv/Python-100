print("Welcome to Chain Calculator")

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

should_continue = True

x = float(input("Enter 1st number : "))
y = float(input("Enter 2nd number : "))
ans = 0

while should_continue:
    print("Choose an operation :- ")
    for i in operations:
        print(i)
    op = input("Operation : ")
    ans = operations[op](x,y)
    print(f"Your result is {ans}")
    should_continue = input("Do you want to perform another operation on this answer? Y/N : ") == "Y"
    if should_continue:
        x = ans
        y = float(input("Enter another number : "))

print(f"\n\nAll operations done!! Your final answer is {ans}")
