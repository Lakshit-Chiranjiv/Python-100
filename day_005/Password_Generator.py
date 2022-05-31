import random
import string
print("Welcome to Password-Generator")

# length,letters(capital,small),numbers,symbols
pass_length = int(input("What would be the length of your password? : "))

num_sm_letters = int(input("How many small-letters? : "))
num_cap_letters = int(input("How many capital-letters? : "))
num_digits = int(input("How many digits? : "))
num_symbols = int(input("How many symbols? : "))


symbols = ['!','@','#','$','%','^','&','*','(',')','+','_']

password = ""

for i in range(1,num_sm_letters+1):
    password += random.choice(string.ascii_lowercase)

for i in range(1,num_cap_letters+1):
    password += random.choice(string.ascii_uppercase)

for i in range(1,num_digits+1):
    password += str(random.randint(0,9))

for i in range(1,num_symbols+1):
    password += symbols[random.randint(0,len(symbols)-1)]

if len(password) < pass_length:
    for i in range(1,pass_length-len(password)+1):
        password += random.choice(string.ascii_lowercase)

password_list = list(password)

random.shuffle(password_list)

password = "".join(password_list)


print("Your password is : "+password)