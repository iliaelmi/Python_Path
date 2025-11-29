# 🔐 Password Generator Tool & Streamlit Dashboard

## 🎯 Description

This project provides a complete **Password Generator System** written in Python, including:

### 🧩 1. Core Password Generator Module (CLI)

Generates three types of passwords:

* **Random Password** → letters + optional digits + optional symbols
* **Pincode** → numeric-only password
* **Memorable Password** → multiple dictionary words (NLTK corpus)

The module includes a **simple command-line interface (CLI)** where the user selects password type and options interactively.

---

### 🖥️ 2. Streamlit Dashboard

A visual, easy-to-use dashboard for generating passwords with:

* Sliders
* Toggles
* Text inputs
* Automatic password generation

It provides a more user-friendly interface for all three password types.

---

## 📂 Project Structure

```
password_generator/
│── main.py                 # Core password generator module + CLI
│── dashboard.py            # Streamlit UI
│── image/
│     └── banner.jpeg       # Banner image used in dashboard
│── README.md               # Documentation
```

---

## 🚀 How to Run

### ✔️ 1. Run the CLI Version

Open terminal in project folder:

```bash
python main.py
```

### ✔️ 2. Run the Streamlit Dashboard

```bash
streamlit run dashboard.py
```

---

## 🧠 Features

### 🔹 CLI Module

* Random password with custom options
* PIN generator
* Memorable passphrase generator
* Fully interactive menu
* Clean code and functions

### 🔹 Streamlit Dashboard

* Graphical interface
* Banner image
* Sliders, toggles, and text fields
* Auto-updating password output
* Uses the same backend functions from `main.py`

---

## 🧪 Example CLI Output

```
=== Password Generator Tool ===
1 - Random Password
2 - PIN Code
3 - Memorable Password (with words)

Choose an option (1/2/3): 1
Enter password length: 12
Include numbers? (y/n): y
Include symbols? (y/n): n

Generated Password: qWab8HcJtLpR
```

---

## 🖼️ Example Streamlit Interface

The dashboard loads a banner image and displays UI elements like radio buttons, sliders, and toggles to generate passwords dynamically.

```
🔐 Password Generator
--------------------
Select a password generator:
  • Random Password
  • Memorable Password
  • Pincode

[slider] Select length: 12
[toggle] Include Numbers: ON
[toggle] Include Symbols: OFF

Your Password is: AbkLpQ73hdWs
```

---

## 📦 Requirements

Install required libraries:

```bash
pip install streamlit nltk
```

For first-time use of memorable passwords, download NLTK word corpus:

```python
import nltk
nltk.download('words')
```
---

## 📄 License

This project is released under the **MIT License** — feel free to use, modify, and distribute it.

---

## 🧑‍💻 Author

**[@iliaelmi](https://github.com/iliaelmi)**
A project created for learning and practicing Python, NLTK, and Streamlit.

---

اگر خواستی می‌تونم نسخه‌ی **فوق حرفه‌ای Markdown با استایل، badge، table of contents و …** هم برات بسازم 🔥
