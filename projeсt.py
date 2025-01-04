import string
import random

letters = string.ascii_letters # biblio with all letters
numbers = string.digits # biblio with all numbers
symbols = string.punctuation # biblio with all symbols

#Hello message and instructions
print("""
      Welcome to the PyPassword Generator!
      You can choose what password you want to construct in this program:
    1) Quick Password: Just enter the total password length, and the program will automatically create a combination.
    2) Custom Password: Choose exactly how many letters, symbols, and numbers your password should contain.
      """)

#Choose the type of password
while True:
    try:
        pass_type = int(input("What type of password would you like? Press 1 for Quick or 2 for Custom\n"))
        if pass_type in [1, 2]:
            break  # Выход из цикла при корректном вводе
        else:
            print("Invalid option. Please choose 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a number.")

#Quick password
if pass_type == 1:
    while True:
        try:
            quick_pass = int(input("How many characters would you like in your password?\n"))
            if quick_pass > 0:  # Проверка на положительное число
                password_list = random.choices(letters + numbers + symbols, k=quick_pass)
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#Custom password
elif pass_type == 2:
    while True:
        try:
            nr_letters = int(input("How many letters would you like in your password?\n"))
            nr_symbols = int(input("How many symbols would you like?\n"))
            nr_numbers = int(input("How many numbers would you like?\n"))
            if nr_letters >= 0 and nr_symbols >= 0 and nr_numbers >= 0:  # Проверка на неотрицательные числа
                if nr_letters + nr_symbols + nr_numbers > 0:  # Проверка, чтобы сумма элементов была больше 0
                    password_list = (random.choices(letters, k=nr_letters) +
                                     random.choices(symbols, k=nr_symbols) +
                                     random.choices(numbers, k=nr_numbers))
                    break
                else:
                    print("The total length of the password must be greater than 0.")
            else:
                print("Please enter non-negative numbers.")
        except ValueError:
            print("Invalid input. Please enter a number.")

#Shuffle adding
random.shuffle(password_list)
password = ''.join(password_list)
print(f"Your password is: {password}")