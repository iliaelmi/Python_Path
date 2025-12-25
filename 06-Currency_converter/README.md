# Currency Converter (CLI & Streamlit)

A simple **currency converter** written in Python.
This project allows you to convert amounts between different currencies using **real-time exchange rates** from the ExchangeRate-API.

It includes:

* **CLI version** for terminal usage (`main.py`)
* **Streamlit version** for a web-based interface (`app.py`)

Designed to practice Python fundamentals, API usage, loops, input validation, and web app development with Streamlit.

---

## 💱 Program Features

* Convert amounts from one currency to another
* Check current exchange rates between currencies
* Supports all currencies provided by the ExchangeRate-API
* CLI version with a menu-driven interface
* Streamlit version with interactive input fields and instant conversion
* Input validation for currency codes and amounts
* Clean and readable project structure

---

## 🧠 Concepts Practiced

* Working with APIs (`requests`)
* Functions and return values
* Loops and menu-driven programs
* Conditional statements
* Input validation
* Docstrings and clean code
* Building a simple web app with Streamlit

---

## ▶️ How to Run CLI Version

1. Make sure you have **Python 3.8+** installed.
2. Clone the repository or download the source code.
3. Install required packages:

```bash
pip install requests
```

4. Run the CLI program:

```bash
python src/main.py
```

---

## ▶️ How to Run Streamlit Version

1. Make sure **Streamlit** is installed:

```bash
pip install streamlit
```

2. Run the Streamlit app:

```bash
streamlit run src/app.py
```

3. The browser will open automatically with the interactive converter.

---

## 🕹️ How to Use

### CLI Version

1. You’ll see a menu:

```
=== Currency Converter Menu ===
1. Convert Currency
2. Check Exchange Rate
3. Exit
```

2. Choose an option by entering **1, 2, or 3**
3. Follow the prompts for currencies and amount
4. Repeat as needed until exiting

### Streamlit Version

* Select the **base currency** and **target currency**
* Enter the **amount to convert**
* Conversion result updates automatically
* No need to press a button; changes are instant

---

## 📂 Project Structure

```
currency_converter/
│
├── README.md       # This file
└── src/
    ├── main.py     # CLI version
    └── app.py      # Streamlit version
```

---

## ✅ Example Output

### CLI

```
=== Currency Converter Menu ===
1. Convert Currency
2. Check Exchange Rate
3. Exit

Enter your choice (1-3): 1
Enter base currency (e.g., USD): USD
Enter target currency (e.g., EUR): EUR
Enter amount in USD: 100

100 USD = 92.50 EUR
```

### Streamlit

* Base Currency: USD
* Target Currency: EUR
* Amount: 100

**Output:** `100 USD = 92.50 EUR` (updates instantly)

---

## 🚀 Possible Improvements

* Add a **GUI version** with more interactive widgets
* Include **automatic list of all supported currencies**
* Handle **API failures and network errors** gracefully
* Save conversion history
* Add **batch conversion mode** for multiple currencies
* Implement **unit tests**
* Deploy the Streamlit app online for web access

---

## 📌 Author

**[@iliaelmi](https://github.com/iliaelmi)**
A learning-oriented project to practice Python, API usage, CLI design, and building simple web apps with Streamlit.
