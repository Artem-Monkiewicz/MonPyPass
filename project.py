import string
import random
import sys  # To terminate the program gracefully

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
    if length <= 0:
        raise ValueError("Length must be a positive integer.")
    return ''.join(random.choices(letters + numbers + symbols, k=length))

# Generate a custom password with specific counts of letters, symbols, and numbers
def generate_custom_password(nr_letters, nr_symbols, nr_numbers):
    """
    Generate a password with a specific number of letters, symbols, and numbers.
    """
    if nr_letters < 0 or nr_symbols < 0 or nr_numbers < 0:
        raise ValueError("All inputs must be non-negative.")
    if nr_letters + nr_symbols + nr_numbers == 0:
        raise ValueError("Total length must be greater than 0.")
    
    # Combine the requested number of characters
    password_list = (random.choices(letters, k=nr_letters) +
                     random.choices(symbols, k=nr_symbols) +
                     random.choices(numbers, k=nr_numbers))
    random.shuffle(password_list)  # Shuffle to ensure randomness
    return ''.join(password_list)

# Main program logic
if __name__ == "__main__":
    try:
        print("""
            Welcome to the PyPassword Generator!
            Choose your preferred password type:
            1) Quick Password: Enter the total length, and we will create a random combination.
            2) Custom Password: Specify how many letters, symbols, and numbers you want.
        """)

        # Get the type of password from the user
        while True:
            try:
                pass_type = int(input("Press 1 for Quick Password or 2 for Custom Password:\n"))
                if pass_type in [1, 2]:
                    break
                else:
                    print("Invalid option. Please choose 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Quick password generation
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

        # Custom password generation
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

        # Display the generated password
        print(f"Your password is: {password}")
    except KeyboardInterrupt:
        handle_exit()
