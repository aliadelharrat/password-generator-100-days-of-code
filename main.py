from random import choice, shuffle
import sys
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()_+-=|;:,.<>?/~`"

print("Welcome to the PyPassword Generator!")
letters_num = int(input("How many letters would you like in your password? "))
symbols_num = int(input("How many symbols would you like? "))
numbers_num = int(input("How many numbers would you like? "))

password = []

if symbols_num + numbers_num > letters_num:
    sys.exit("The combined number of symbols and digits cannot exceed the number of letters.")

for _ in range(symbols_num):
    password.append(choice(symbols))

for _ in range(numbers_num):
    password.append(str(choice(range(10))))

while len(password) < letters_num:
    password.append(choice(alphabet))

shuffle(password)
generated_password = "".join(password)

print(f"Here is your password: '{generated_password}'")
