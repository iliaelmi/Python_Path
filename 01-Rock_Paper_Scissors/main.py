import random


class RockPaperScissors:
    """
    A simple Rock-Paper-Scissors game for a single player against the computer.

    Attributes:
        choices (list): Available options for the game.
        rounds (int): Number of rounds per game session.
        player_score (int): Tracks the player's score.
        computer_score (int): Tracks the computer's score.
    """

    def __init__(self):
        """Initialize the game with default settings."""
        self.choices = ["rock", "paper", "scissors"]
        self.rounds = 3
        self.player_score = 0
        self.computer_score = 0

    @staticmethod
    def start_game():
        """
        Display the welcome screen and prompt the user to start the game.

        Exits the program if the user inputs 'Q' or 'q'.
        """
        print("=================================")
        print("    Welcome to RockPaperScissors")
        print("           Are you ready?")
        print("=================================")
        start = input("Press ENTER to start (Q/q to exit): ").strip()

        if start.lower() == "q":
            print("\nExiting the game...")
            exit()

    def get_player_choice(self):
        """
        Prompt the player to select a choice from the available options.

        Returns:
            str: The player's choice ('rock', 'paper', or 'scissors').

        Loops until the player enters a valid option.
        """
        while True:
            player_choice = input(f"Enter your choice ({self.choices}): ").strip().lower()
            if player_choice in self.choices:
                return player_choice
            print(f"Invalid choice, you must select from {self.choices}.")

    def computer_choice(self):
        """
        Randomly select a choice for the computer.

        Returns:
            str: The computer's choice ('rock', 'paper', or 'scissors').
        """
        return random.choice(self.choices)

    def decide_winner(self, user_choice, computer_choice):
        """
        Determine the winner of a single round.

        Args:
            user_choice (str): Player's selected choice.
            computer_choice (str): Computer's selected choice.

        Returns:
            str: 'player' if the player wins, 'computer' if the computer wins,
                 'tie' if the round is a draw.
        """
        if user_choice == computer_choice:
            return "tie"

        WIN_RULES = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

        if WIN_RULES[user_choice] == computer_choice:
            return "player"
        return "computer"

    def play(self):
        """
        Play a full game session consisting of multiple rounds.

        For each round:
            - Prompt the player for their choice.
            - Randomly generate the computer's choice.
            - Determine the winner and update scores.
            - Display round results.

        After all rounds, display the final scores.
        """
        for r in range(1, self.rounds + 1):
            print(f"\n--- Round {r} ---")
            user_choice = self.get_player_choice()
            computer_choice = self.computer_choice()
            print(f"Computer chose: {computer_choice}")

            result = self.decide_winner(user_choice, computer_choice)

            if result == "player":
                self.player_score += 1
                print("You won this round!")
            elif result == "computer":
                self.computer_score += 1
                print("Computer won this round!")
            else:
                print("This round is a tie.")

        print("\n=== Final Results ===")
        print(f"You: {self.player_score}")
        print(f"Computer: {self.computer_score}")


# ---------------------------
# MAIN EXECUTION
# ---------------------------

RockPaperScissors.start_game()
game = RockPaperScissors()

while True:
    game.play()
    again = input("\nPress ENTER to play again (Q/q to quit): ").strip().lower()
    if again == "q":
        print("Goodbye!")
        break 

if __name__ == "__main__":
    main()
