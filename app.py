import streamlit as st  # type:ignore

st.set_page_config(page_title="Password Strength Meter", layout="centered")

import sys
from password_strength import PasswordStats  # type:ignore

st.write("Python Executable:", sys.executable)
st.write("Python Version:", sys.version)

st.markdown(
    """
    <style>
    /* Gradient Background */
    body {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        font-family: 'Orbitron', sans-serif;
    }

    /* Glassmorphic Container */
    .glass-container {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 2px solid rgba(255, 255, 255, 0.2);
        text-align: center;
        max-width: 500px;
        margin: auto;
        animation: fadeIn 1.2s ease-in-out;
    }

    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: scale(0.9); }
        to { opacity: 1; transform: scale(1); }
    }

    /* Styled Input Field */
    .stTextInput input {
        background: rgba(255, 255, 255, 0.2) !important;
        border-radius: 15px;
        padding: 12px;
        border: 2px solid rgba(0, 255, 255, 0.5);
        color: black !important;
        font-size: 18px;
        text-align: center;
        box-shadow: 0 0 12px rgba(0, 255, 255, 0.5);
        transition: 0.3s ease-in-out;
    }

    /* Password Strength Messages */
    .weak {
        color: #ff4b2b !important;
        font-weight: bold;
    }
    .moderate {
        color: #ff9800 !important;
        font-weight: bold;
    }
    .strong {
        color: #00c853 !important;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():
    st.markdown('<div class="glass-container">', unsafe_allow_html=True)
    st.title("🔮 Password Strength Meter")

    password = st.text_input("Enter your password", type="password", placeholder="Type your password...")

    if password:
        stats = PasswordStats(password)
        strength = stats.strength()

        if strength < 0.3:
            st.markdown('<p class="weak">❌ Weak Password</p>', unsafe_allow_html=True)
            color = "#ff4b2b"
        elif strength < 0.6:
            st.markdown('<p class="moderate">⚠️ Moderate Password</p>', unsafe_allow_html=True)
            color = "#ff9800"
        else:
            st.markdown('<p class="strong">✅ Strong Password</p>', unsafe_allow_html=True)
            color = "#00c853"

        st.markdown(
            f"""
            <style>
            .stProgress > div > div > div {{
                background: {color} !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

        st.progress(strength)

    st.markdown('</div>', unsafe_allow_html=True)
