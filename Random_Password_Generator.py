import string
import secrets

def make_secure_password(length=32, include_uppercase=True, include_numbers=True, include_symbols=True):
    chars = string.ascii_lowercase
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_numbers:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation

    while True:
        password = "".join(secrets.choice(chars) for _ in range(length))
        conditions = [any(c in string.ascii_lowercase for c in password)]

        if include_uppercase:
            conditions.append(any(c in string.ascii_uppercase for c in password))
        if include_numbers:
            conditions.append(any(c in string.digits for c in password))
        if include_symbols:
            conditions.append(any(c in string.punctuation for c in password))

        if all(conditions):
            return password

if __name__ == "__main__":
    print("Password Examples:")
    print(f"Default Password (32): {make_secure_password()}")
    print(f"Easy Password (8, no numbers): {make_secure_password(length=8, include_numbers=False)}")
