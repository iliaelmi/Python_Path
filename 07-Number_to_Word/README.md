# Number to Words Converter (CLI)

A simple **number-to-words converter** written in Python.  
This project allows you to convert any integer (including negative numbers) into **English words**.

It includes:

* **CLI version** for terminal usage (`src/main.py`)

Designed to practice Python fundamentals, recursion, loops, input validation, and CLI design.

---

## 🔢 Program Features

* Convert integers to English words
* Supports numbers from negative to positive (including zero)
* CLI version with a **menu-driven interface**
* Input validation for integers
* Clean and readable project structure

---

## 🧠 Concepts Practiced

* Recursion and function calls
* Conditional statements (`if`, `elif`, `else`)
* Loops and menu-driven programs
* Input validation
* Using constants and dictionaries
* Clean code and docstrings
* CLI design and user interaction

---

## ▶️ How to Run CLI Version

1. Make sure you have **Python 3.8+** installed.
2. Clone the repository or download the source code.
3. Navigate to the `src/` folder.
4. Run the CLI program:

```bash
python main.py
```

---

## 🕹️ How to Use

### CLI Version

1. You’ll see a menu:

```
========================================
 Number to Words Converter
========================================
1. Convert a number
2. Exit
```

2. Choose an option by entering **1** or **2**
3. If you choose **1**, enter the number you want to convert
4. The program will display the number in words, e.g.:

```
Enter a number: -342
Result: Minus Three Hundred Forty-Two
```

5. Repeat as needed until exiting

---

## 📂 Project Structure

```
number_to_words/
│
├── README.md        # This file
└── src/
    ├── main.py      # CLI program
    └── constans.py  # Contains constants like under_20, tens, above_100
```

---

## ✅ Example Output

### CLI

```
========================================
 Number to Words Converter
========================================
1. Convert a number
2. Exit

Enter your choice (1/2): 1
Enter a number: -342

Result: Minus Three Hundred Forty-Two
```

---

## 🚀 Possible Improvements

* Add **decimal number support**
* Implement a **GUI or web-based version** with Streamlit
* Save conversion history
* Add **unit tests**
* Allow batch conversion for multiple numbers
* Support multiple languages

---

## 📌 Author

**[@iliaelmi](https://github.com/iliaelmi)**  
A learning-oriented project to practice Python, recursion, CLI design, and clean code.

