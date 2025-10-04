from random import choice, shuffle
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()_+-=|;:,.<>?/~`"

print("Welcome to the PyPassword Generator!")
letters_num = int(input("How many letters would you like in your password? "))
symbols_num = int(input("How many symbols would you like? "))
numbers_num = int(input("How many numbers would you like? "))

generated_password = ""

for _ in range(symbols_num):
    generated_password += choice(symbols)

for _ in range(numbers_num):
    generated_password += str(choice(range(9)))

while len(generated_password) < letters_num:
    generated_password += choice(alphabet)

generated_password_list = list(generated_password)
shuffle(generated_password_list)
generated_password = "".join(generated_password_list)

print(f"Here is your password: '{generated_password}'")
