import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    # Set base characters to letters
    characters = string.ascii_letters

    # Add digits if the checkbox is checked
    if use_digits:
        characters += string.digits  # add numbers

    # Add special characters if the checkbox is checked
    if use_special:
        characters += string.punctuation  # add special characters

    # Generate a random password from the available characters
    return "".join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title("Password Generator")

# Slider for password length
length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)

# Checkbox options for including digits and special characters
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

# Button to generate the password
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password: {password}")

# Footer
st.write("-----------------------")
st.write("Made by Syeda")
