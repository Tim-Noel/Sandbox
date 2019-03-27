"""
Tim Noel
"""

MIN_LENGTH = 4


def version_1():
    password = input("Please enter password with at least {} characters: ".format(MIN_LENGTH))
    while len(password) < MIN_LENGTH:
        password = input("Pleas enter a  password with at least {} characters: ".format(MIN_LENGTH))

    print('*' * len(password))


def main():
    """Get and print password using functions."""
    password = get_password(MIN_LENGTH)
    print_asterisks(password)


def get_password(min_length):
    """Get password, ensuring it meets the minimum_length requirement."""
    password = input("Enter password of at least {} characters: ".format(min_length))
    while len(password) < min_length:
        print("Password too short")
        password = input("Enter password of at least {} characters: ".format(min_length))
    return password


def print_asterisks(sequence):
    """Print as many asterisks as there are characters in the passed-in sequence."""
    print('*' * len(sequence))


main()
