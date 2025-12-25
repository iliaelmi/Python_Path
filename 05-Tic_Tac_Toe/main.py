import random
from typing import List


class Tic_Tac_Toe:
    """
    A simple command-line Tic-Tac-Toe game for two players.

    The game board uses indexes 1 to 9:
        1 | 2 | 3
        --+---+--
        4 | 5 | 6
        --+---+--
        7 | 8 | 9
    """

    def __init__(self) -> None:
        """
        Initialize the game board and randomly select the first player.
        """
        # Board positions are strings so numbers can be replaced by 'X' or 'O'
        self.board: List[str] = list(map(str, range(10)))

        # Randomly choose which player starts
        self.player: str = random.choice("XO")

    def show_board(self) -> None:
        """
        Display the current state of the game board.
        """
        print()
        print(f"{self.board[1]} | {self.board[2]} | {self.board[3]}")
        print("--+---+--")
        print(f"{self.board[4]} | {self.board[5]} | {self.board[6]}")
        print("--+---+--")
        print(f"{self.board[7]} | {self.board[8]} | {self.board[9]}")
        print()

    def decide_winner(self, player: str) -> bool:
        """
        Check whether the given player has won the game.

        Args:
            player (str): The player symbol ('X' or 'O').

        Returns:
            bool: True if the player has a winning combination, False otherwise.
        """
        win_comb: List[List[int]] = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],   # Rows
            [1, 4, 7], [2, 5, 8], [3, 6, 9],   # Columns
            [1, 5, 9], [3, 5, 7]               # Diagonals
        ]

        for win in win_comb:
            if all(self.board[cell] == player for cell in win):
                return True
        return False

    def swap_player_turn(self) -> str:
        """
        Switch the current player from X to O or from O to X.

        Returns:
            str: The new current player.
        """
        self.player = "O" if self.player == "X" else "X"
        return self.player

    def is_board_filled(self) -> bool:
        """
        Check whether the board is completely filled.

        Returns:
            bool: True if no empty positions remain, False otherwise.
        """
        return all(cell in ["X", "O"] for cell in self.board[1:])

    def fix_spot(self, cell: int, player: str) -> None:
        """
        Place the player's mark on the selected cell.

        Args:
            cell (int): Board position (1-9).
            player (str): Player symbol ('X' or 'O').
        """
        self.board[cell] = player

    def start(self) -> None:
        """
        Start the main game loop.
        Handles player input, board updates, and game termination.
        """
        print("Welcome to Tic-Tac-Toe!")
        print(f"Player {self.player} goes first.")

        while True:
            self.show_board()
            print(f"Player {self.player}'s turn.")

            # Get user input
            cell: int = int(input("Choose a position (1-9): "))

            # Validate the move
            if cell in range(1, 10) and self.board[cell] == str(cell):
                self.fix_spot(cell, self.player)

                # Check for a win
                if self.decide_winner(self.player):
                    self.show_board()
                    print(f"Player {self.player} wins!")
                    break

                # Check for a draw
                if self.is_board_filled():
                    self.show_board()
                    print("It's a draw!")
                    break

                # Switch turns
                self.swap_player_turn()
            else:
                print("Invalid move. Please choose an empty position between 1 and 9.")


if __name__ == "__main__":
    game: Tic_Tac_Toe = Tic_Tac_Toe()
    game.start()
