# 📘 Contact Book Application

## 📖 Description

A clean and user-friendly **Contact Management System** written in Python.
This program allows you to easily:

* ➕ Add new contacts
* ✏️ Edit existing contacts
* 📄 View all contacts
* ❌ Delete contacts
* 🔍 Validate user input (names & phone numbers)
* 🎛️ Use an organized, menu-driven CLI

Designed using **OOP**, clean code practices, and fully documented with **docstrings**.

---

## 🗂️ Project Structure

```
contact_book/
│── main.py        # Main application with CLI menu + ContactBook class
│── README.md      # Documentation
```

---

## ▶️ How to Run

Open terminal and run:

```bash
python main.py
```

This starts the interactive Contact Book menu.

---

## ⭐ Features

### 🧩 Core Functions

* Add contact (name, phone, email)
* Edit phone or email of any existing contact
* View all contacts in a clean formatted list
* Delete contacts safely

### 🔐 Input Validation

* ✔️ Name: alphabetic characters only
* ✔️ Phone: must be numeric
* ✔️ Phone length: exactly 11 digits

### 🧱 Code Quality

* Object-Oriented design
* Clean, readable, PEP-8 compliant
* Well-structured and reusable functions
* Full docstring documentation

---

## 📤 Example Output

```
========================================
            CONTACT BOOK
========================================
1. Add Contact
2. Edit Contact
3. View Contacts
4. Delete Contact
5. Quit
----------------------------------------
Choose an option: 1

Enter contact name: John Doe
Enter contact phone number: 09123456789
Enter contact email (optional): john@example.com

Contact added successfully.
```

---

## 📦 Requirements

This project uses **only Python standard libraries**.
No additional installation is needed.

---

## 👨‍💻 Author

**[@iliaelmi](https://github.com/iliaelmi)**
A learning-oriented project created to practice Python, OOP, validation logic, and CLI design.

---
