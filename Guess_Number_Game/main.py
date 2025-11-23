import random

def validate_input(user_input):
    """
    Validates the user's input to ensure it is a number between 1 and 100.
    
    Args:
        user_input (str): Input string from the user.
    
    Returns:
        int | bool: Returns the integer value if valid, otherwise False.
    """
    if not user_input.isdigit():
        print("Invalid input, please enter digits")
        return False

    user_input = int(user_input)
    if user_input < 1 or user_input > 100:
        print("Your guess is out of range (1-100)")
        return False

    return user_input


def main():
    """
    Main game loop for the number guessing game.
    Generates a random number and prompts the user to guess it until correct or quit.
    """
    system_random = random.randint(1, 100)
    counter = 0  # Tracks number of valid guesses

    print("Welcome to the Guessing Game!")
    print("Try to guess the number between 1 and 100.")
    print("Type 'q' to quit at any time.\n")

    while True:
        user_input = input("Enter your guess: ").strip()

        # Allow quitting the game
        if user_input.lower() == "q":
            print("Goodbye! Have a nice day.")
            break

        valid_input = validate_input(user_input)
        if not valid_input:
            continue  # Invalid input, ask again

        user_input = valid_input
        counter += 1  # Increment counter only for valid guesses

        # Compare guess with the generated number
        if user_input == system_random:
            print(f"Congratulations! You guessed the number in {counter} guess{'es' if counter > 1 else ''}!")
            break
        elif user_input > system_random:
            print("My number is lower. Try again!\n")
        else:
            print("My number is higher. Guess again!\n")


if __name__ == "__main__":
    main()
