# Tic-Tac-Toe (CLI)

A simple **command-line Tic-Tac-Toe game** written in Python using Object-Oriented Programming (OOP).
This project is designed for practice with core Python concepts such as classes, methods, control flow, and type annotations.

---

## 🎮 Game Features

- Two-player turn-based gameplay (X vs O)
- Randomly selects which player starts
- Clear board display with numbered positions
- Input validation for moves
- Win detection (rows, columns, diagonals)
- Draw detection when the board is full
- Clean and readable game flow

---

## 🧠 Concepts Practiced

- Object-Oriented Programming (OOP)
- Class design and methods
- Game loop logic
- Conditional statements
- List manipulation
- Type annotations (PEP 484)
- Docstrings and clean code structure

---

## 🗺️ Board Layout

The board positions are numbered as follows:

```

1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9

````

Players choose a position by entering a number from **1 to 9**.

---

## ▶️ How to Run

1. Make sure you have Python 3.8+ installed.
2. Clone the repository or download the source code.
3. Run the game from the terminal:

```bash
python main.py
````

---

## 🕹️ How to Play

* The game will randomly choose which player (`X` or `O`) goes first.
* On your turn, enter a number between **1 and 9** to place your mark.
* You cannot choose an already occupied position.
* The game ends when:

  * A player wins, or
  * The board is full (draw).

---

## 📂 Project Structure

```
tic_tac_toe/
│
├── main.py
└── README.md
```

---

## ✅ Example Output

```
Player X's turn.
Choose a position (1-9): 5

X | 2 | 3
--+---+--
4 | X | 6
--+---+--
7 | 8 | 9
```

---

## 🚀 Possible Improvements

* Add AI player (random or minimax)
* Restart game option
* Input error handling with try/except
* Colored terminal output
* Unit tests with pytest
* GUI version (Tkinter / Pygame)

---

## 📌 Author
**[@iliaelmi](https://github.com/iliaelmi)**
A learning-oriented project created to practice Python, OOP, validation logic, and CLI design.

```
