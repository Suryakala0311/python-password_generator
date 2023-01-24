import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

input1 = int(input("How many letters would you like to have in your password? \n"))
input2 = int(input("How many symbols would you like to have in your password? \n"))
input3 = int(input("How many numbers would you liketo have in your password? \n"))

password = ""
for i in range(0, input1):
    password += random.choice(letters)

for j in range(0, input2):
    password += random.choice(numbers)

for k in range(0, input3):
    password += random.choice(symbols)

l = list(password)
random.shuffle(l)
new_password = ''.join(l)

print(f"Here is your password: {new_password}")
