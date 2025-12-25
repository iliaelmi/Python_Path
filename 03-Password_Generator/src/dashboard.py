"""
Password Generator Dashboard using Streamlit
-------------------------------------------
This app provides 3 types of password generators:

1. Random Password:
   - Generates a password with letters, optional digits, and optional symbols.

2. Memorable Password:
   - Generates a passphrase based on dictionary words with a custom separator.

3. Pincode:
   - Generates a numeric PIN of custom length.

Author: Your Name
"""

import streamlit as st
from main import Random_Password, Memorable_Password, Pincode
from nltk.corpus import words


# ------------------------------------------------------
#   HEADER SECTION
# ------------------------------------------------------

# Show banner image
st.image(r'F:\python programing\password_generator\image\banner.jpeg')

# Title of the dashboard
st.title(':spider_web: Password Generator')


# ------------------------------------------------------
#   USER OPTION SELECTION
# ------------------------------------------------------

# Radio button menu for selecting password type
option = st.radio(
    'Select a password generator',
    ("Random Password", "Memorable Password", "Pincode")
)


# ------------------------------------------------------
#   RANDOM PASSWORD GENERATOR
# ------------------------------------------------------
if option == "Random Password":

    # Slider to choose password length
    length = st.slider("Select the length of password", 4, 20)

    # Toggles for extra options
    include_number = st.toggle('Include Number')
    include_symbol = st.toggle('Include Symbol')

    # Generate the password using the imported function
    generator = Random_Password(length, include_number, include_symbol)

    # Display the result
    st.write(f"Your Password is : {generator}")


# ------------------------------------------------------
#   MEMORABLE PASSWORD GENERATOR
# ------------------------------------------------------
elif option == "Memorable Password":

    # Number of words in passphrase
    length = st.slider("Select number of words:", 4, 20)

    # User-defined separator between words
    separator = st.text_input("Separator", value='-')

    # Generate memorable (word-based) password
    generator = Memorable_Password(length, separator)

    # Show output
    st.write(f"Your Password is : {generator}")


# ------------------------------------------------------
#   PINCODE GENERATOR
# ------------------------------------------------------
elif option == "Pincode":

    # Length of numeric PIN
    length = st.slider("Select PIN length:", 4, 20)

    # Call numeric-only PIN generator
    generator = Pincode(length)

    # Display PIN result
    st.write(f"Your PIN Code is : {generator}")
