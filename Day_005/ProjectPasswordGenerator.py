# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
# numbers = ['0','1','2','3','4','5','6','7','8','9']
# symbols =['!','@','#','$','%','&','*','(',')']
# print("Welcome to the password generator!")
# no_letters = int(input("How many letters do you want in your password?"))
# no_symbols = int(input("How many symbols do you want in your password?"))
# no_numbers = int(input("How many numbers do you want in your password?"))
# password = ""
# for i in range(0, no_letters):
#     password += random.choice(letters)
# for j in range(0, no_symbols):
#     password += random.choice(numbers)
# for k in range(0, no_numbers):
#     password += random.choice(symbols)
# print(password)
# --------------------------------------------------------------------
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols =['!','@','#','$','%','&','*','(',')']
print("Welcome to the password generator!")
no_letters = int(input("How many letters do you want in your password?"))
no_symbols = int(input("How many symbols do you want in your password?"))
no_numbers = int(input("How many numbers do you want in your password?"))
password_list = []
for char in range(0, no_letters):
    password_list.append(random.choice(letters))
for char in range(0, no_symbols):
    password_list.append(random.choice(numbers))
for char in range(0, no_numbers):
    password_list.append(random.choice(symbols))
print(password_list)
password = ""
for char in password_list:
    password += char
print(f"your password is: {password}")
