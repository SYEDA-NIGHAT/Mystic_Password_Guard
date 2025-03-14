import streamlit as st # type:ignore
import random
import string
import re

# Configure page settings
st.set_page_config(page_title="Password Strength Meter", layout="centered", page_icon="🔐")

# Apply light theme styles
st.markdown(
    """
    <style>
    /* Light theme background */
    .stApp {
        background-color: white !important;
        color: black !important;
    }

    /* Input labels - black text */
    label {
        color: black !important;
        font-weight: bold;
    }

    /* Input fields - black text on white background */
    .stTextInput>div>div>input {
        background-color: white !important;
        color: black !important;
        font-weight: bold !important;
        text-align: center !important;
        border-radius: 10px;
        border: 2px solid #ccc;
        padding: 8px;
    }

    /* Slider text and labels */
    .stSlider {
        color: black !important;
    }

    /* Button styling */
    .stButton>button {
        background-color: #007BFF !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 5px;
        padding: 10px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #0056b3 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Password Strength Checker
st.markdown("## 🔍 Check Password Strength")
password = st.text_input("Enter your password:", type="password")

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1

    if strength == 5:
        return "Strong 💪", "green" 
    elif strength >= 3:
        return "Medium 🟠", "orange"
    elif strength >= 1:
        return "Weak ❌", "red"
    else:
        return "Invalid! Please enter a password", "black"


if password:
    strength, color = check_password_strength(password)
    st.markdown(f"**Password Strength: <span style='color:{color};'>{strength}</span>**", unsafe_allow_html=True)

# Password Generator
st.markdown("## ⚡ Generate a Strong Password")
length = st.slider("Select password length", min_value=8, max_value=24, value=12)
generate_btn = st.button("Generate Password")

if generate_btn:
    generated_password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    st.text_input("Generated Password:", value=generated_password, key="generated_password")

