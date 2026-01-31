import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4"

    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%&*"

    password_chars = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars = letters + digits + symbols

    while len(password_chars) < length:
        password_chars.append(random.choice(all_chars))

    random.shuffle(password_chars)
    return "".join(password_chars)

print("\n--- PASSWORD GENERATOR ---")
try:
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number")
