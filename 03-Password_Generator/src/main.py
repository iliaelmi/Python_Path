"""
Password Generator Module
-------------------------

This module provides three types of password generators:

1. Random_Password:
   Generates a fully random password with letters, optional digits,
   and optional symbols.

2. Pincode:
   Generates a numeric-only PIN of a custom length.

3. Memorable_Password:
   Generates a passphrase using dictionary words from the NLTK corpus.

It also includes a command-line interface (CLI) for interactive usage.
"""

import random
import string
import nltk


# ------------------------------------------------------
#   RANDOM PASSWORD GENERATOR
# ------------------------------------------------------
def Random_Password(length, include_number=False, include_symbol=False):
    """
    Generate a random password.

    Parameters:
        length (int):
            Length of the password.
        include_number (bool, optional):
            Include digits (0-9) in the password. Default is False.
        include_symbol (bool, optional):
            Include punctuation symbols in the password. Default is False.

    Returns:
        str: A randomly generated password.
    """

    # Start with alphabet characters (uppercase + lowercase)
    characters = string.ascii_letters

    # Add digits if user enabled the option
    if include_number:
        characters += string.digits

    # Add symbols if enabled
    if include_symbol:
        characters += string.punctuation

    # Randomly generate password from character pool
    return ''.join(random.choice(characters) for _ in range(length))


# ------------------------------------------------------
#   NUMERIC PIN GENERATOR
# ------------------------------------------------------
def Pincode(length):
    """
    Generate a numeric-only PIN code.

    Parameters:
        length (int):
            Number of digits in the PIN.

    Returns:
        str: A PIN consisting only of digits.
    """

    # Only digits 0–9
    return ''.join(random.choice(string.digits) for _ in range(length))


# ------------------------------------------------------
#   MEMORABLE (WORD-BASED) PASSWORD GENERATOR
# ------------------------------------------------------
def Memorable_Password(length, separator="_"):
    """
    Generate a memorable password using dictionary words.

    Parameters:
        length (int):
            Number of words to include in the passphrase.
        separator (str, optional):
            Character(s) used between words. Default is "_".

    Returns:
        str: A passphrase created from random dictionary words.
    """

    # Load the list of dictionary words from NLTK
    words_list = nltk.corpus.words.words()

    # Select random words and join them using the separator
    return separator.join(random.choice(words_list) for _ in range(length))


# ------------------------------------------------------
#   MAIN CLI MENU
# ------------------------------------------------------
def main():
    """
    Command-line interface for the Password Generator Tool.

    Allows the user to choose between:
        1. Random Password
        2. Numeric PIN
        3. Memorable (word-based) Password
    """

    print("=== Password Generator Tool ===")
    print("1 - Random Password")
    print("2 - PIN Code")
    print("3 - Memorable Password (with words)")

    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        # Random password settings
        length = int(input("Enter password length: "))
        include_number = input("Include numbers? (y/n): ").lower() == "y"
        include_symbol = input("Include symbols? (y/n): ").lower() == "y"

        print("Generated Password:",
              Random_Password(length, include_number, include_symbol))

    elif choice == "2":
        # PIN generator
        length = int(input("Enter PIN length: "))
        print("Generated PIN:", Pincode(length))

    elif choice == "3":
        # Memorable (word-based) password
        length = int(input("How many words?: "))
        print("Generated Memorable Password:",
              Memorable_Password(length))

    else:
        print("Invalid choice!")


# ------------------------------------------------------
#   RUN IF EXECUTED DIRECTLY
# ------------------------------------------------------
if __name__ == "__main__":
    main()

