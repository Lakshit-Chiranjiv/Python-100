import string


print("Welcome to caesar cipher!!")

choice = int(input("Choose ENCODE OR DECODE\nenter 1 to encode\nenter 2 to decode\nyour choice : "))
operation=''
m = 1
if choice==1:
    operation = 'encode'
elif choice==2:
    operation = 'decode'
    m = -1
else:
    print("Invalid choice")

if choice==1 or choice==2:
    input_text = input("Enter a string to "+operation+" : ")
    shift = int(input("Enter shift value : "))

    letters = list(string.ascii_lowercase)

    final_text = ''
    shift *= m
    for i in input_text:
        pos = letters.index(i)
        final_text += letters[pos+shift]

    print(f"Your {operation}d text is : {final_text}")