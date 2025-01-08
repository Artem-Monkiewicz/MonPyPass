import string
import random
import sys  # To terminate the program gracefully
import logging


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log",
    filemode="a",
)


# Define character sets for the password
letters = string.ascii_letters  # All uppercase and lowercase letters
numbers = string.digits  # Digits from 0 to 9
symbols = string.punctuation  # Common symbols like !, @, #

# Handle program exit
def handle_exit():
    """
    Gracefully exits the program with a goodbye message.
    """
    print("\nGoodbye! Thank you for using PyPassword Generator. Stay secure! 🔒")
    sys.exit(0)

# Generate a quick password with a given length
def generate_quick_password(length):
    """
    Generate a random password of the specified length using letters, numbers, and symbols.
    """
    logging.info(f"Generating a quick password with length: {length}")
    if length <= 0:
        logging.error("Password length must be a positive integer.")
        raise ValueError("Length must be a positive integer.")
    return ''.join(random.choices(letters + numbers + symbols, k=length))

# Generate a custom password with specific counts of letters, symbols, and numbers
def generate_custom_password(nr_letters, nr_symbols, nr_numbers):
    """
    Generate a password with a specific number of letters, symbols, and numbers.
    """
    logging.info(f"Generating a custom password: {nr_letters} letters, {nr_symbols} symbols, {nr_numbers} numbers.")
    if nr_letters < 0 or nr_symbols < 0 or nr_numbers < 0:
        logging.error("Inputs for custom password must be non-negative.")
        raise ValueError("All inputs must be non-negative.")
    if nr_letters + nr_symbols + nr_numbers == 0:
        logging.error("Total length of custom password must be greater than 0.")
        raise ValueError("Total length must be greater than 0.")

    password_list = (random.choices(letters, k=nr_letters) +
                     random.choices(symbols, k=nr_symbols) +
                     random.choices(numbers, k=nr_numbers))
    random.shuffle(password_list)
    return ''.join(password_list)

def check_password_strength(password):
    """
    Evaluate the strength of a password.
    Returns a string indicating the strength level: Weak, Medium, or Strong.
    """
    length = len(password)
    has_letters = any(char.isalpha() for char in password)
    has_numbers = any(char.isdigit() for char in password)
    has_symbols = any(char in string.punctuation for char in password)
    unique_chars = len(set(password))

    logging.info(f"Checking password strength for: {password}")
    if length < 8 or unique_chars < 4:
        return "Weak"
    elif length >= 8 and has_letters and has_numbers and (has_symbols or unique_chars > 6):
        return "Medium"
    elif length >= 12 and has_letters and has_numbers and has_symbols:
        return "Strong"
    else:
        return "Weak"


if __name__ == "__main__":
    try:
        print("""
            Welcome to the PyPassword Generator!
            Choose your preferred password type:
            1) Quick Password: Enter the total length, and we will create a random combination.
            2) Custom Password: Specify how many letters, symbols, and numbers you want.
        """)
        while True:
            try:
                pass_type = int(input("Press 1 for Quick Password or 2 for Custom Password:\n"))
                if pass_type in [1, 2]:
                    break
                else:
                    print("Invalid option. Please choose 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if pass_type == 1:
            while True:
                try:
                    quick_pass = int(input("Enter the total number of characters for your password:\n"))
                    if quick_pass > 0:
                        password = generate_quick_password(quick_pass)
                        break
                    else:
                        print("Please enter a positive number.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        elif pass_type == 2:
            while True:
                try:
                    nr_letters = int(input("How many letters would you like in your password?\n"))
                    nr_symbols = int(input("How many symbols would you like?\n"))
                    nr_numbers = int(input("How many numbers would you like?\n"))
                    if nr_letters >= 0 and nr_symbols >= 0 and nr_numbers >= 0:
                        if nr_letters + nr_symbols + nr_numbers > 0:
                            password = generate_custom_password(nr_letters, nr_symbols, nr_numbers)
                            break
                        else:
                            print("The total length must be greater than 0.")
                    else:
                        print("Please enter non-negative numbers.")
                except ValueError:
                    print("Invalid input. Please enter valid numbers.")

        # Output password
        print(f"Your password is: {password}")

        # Checking password complexity
        strength = check_password_strength(password)
        print(f"Password strength: {strength}")

        logging.info("Password generated successfully.")

    except KeyboardInterrupt:
        handle_exit()