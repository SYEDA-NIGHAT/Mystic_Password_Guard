# import streamlit as st
# from password_strength import PasswordStats

# # ---- Enthusiastic Glassmorphism & Modern Styling ----
# st.markdown(
#     """
#     <style>
#     /* Full Page Background */
#     body {
#         background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
#         font-family: 'Poppins', sans-serif;
#     }
    
#     /* Glassmorphic Card */
#     .glass-container {
#         background: rgba(255, 255, 255, 0.1);
#         border-radius: 20px;
#         padding: 40px;
#         box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
#         backdrop-filter: blur(15px);
#         -webkit-backdrop-filter: blur(15px);
#         border: 2px solid rgba(255, 255, 255, 0.3);
#         text-align: center;
#         max-width: 500px;
#         margin: auto;
#     }

#     /* Password Input Field */
#     .stTextInput input {
#         background: rgba(255, 255, 255, 0.2) !important;
#         border-radius: 15px;
#         padding: 12px;
#         border: 2px solid rgba(255, 255, 255, 0.4);
#         color: white !important;
#         font-size: 18px;
#         font-weight: bold;
#         text-align: center;
#         box-shadow: inset 0 0 10px rgba(255, 255, 255, 0.2);
#     }
    
#     .stTextInput input::placeholder {
#         color: rgba(255, 255, 255, 0.7);
#         font-weight: normal;
#     }

#     /* Heading Style */
#     h1 {
#         font-family: 'Poppins', sans-serif;
#         color: white;
#         text-shadow: 3px 3px 8px rgba(0,0,0,0.3);
#         font-size: 36px;
#     }

#     /* Progress Bar with Gradient Animation */
#     .stProgress > div > div > div {
#         border-radius: 12px;
#         background: linear-gradient(270deg, #ff416c, #ff4b2b, #ff7300);
#         transition: all 0.5s ease-in-out;
#     }
    
#     /* Password Strength Messages */
#     .weak {
#         color: #ff4b2b !important;
#         font-weight: bold;
#     }
#     .moderate {
#         color: #ff9800 !important;
#         font-weight: bold;
#     }
#     .strong {
#         color: #00c853 !important;
#         font-weight: bold;
#     }
    
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # ---- UI Layout ----
# st.markdown('<div class="glass-container">', unsafe_allow_html=True)
# st.title("🔮 Password Strength Meter")

# password = st.text_input("Enter your password", type="password", placeholder="Type your password...")

# if password:
#     stats = PasswordStats(password)
#     strength = stats.strength()
    
#     if strength < 0.3:
#         st.markdown('<p class="weak">❌ Weak Password</p>', unsafe_allow_html=True)
#         color = "#ff4b2b"
#     elif strength < 0.6:
#         st.markdown('<p class="moderate">⚠️ Moderate Password</p>', unsafe_allow_html=True)
#         color = "#ff9800"
#     else:
#         st.markdown('<p class="strong">✅ Strong Password</p>', unsafe_allow_html=True)
#         color = "#00c853"

#     # Apply custom progress bar color dynamically
#     st.markdown(
#         f"""
#         <style>
#         .stProgress > div > div > div {{
#             background: {color} !important;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )
    
#     st.progress(strength)

# st.markdown('</div>', unsafe_allow_html=True)

# import streamlit as st # type:ignore
# from password_strength import PasswordStats # type:ignore

# # ---- Set page layout ----
# st.set_page_config(page_title="Password Strength Meter", layout="centered")

# # ---- Create a centered container ----
# with st.container():
#     st.title("🔮 Password Strength Meter")

#     # Password input
#     password = st.text_input("Enter your password", type="password", placeholder="Type your password...")

#     # Strength calculation
#     if password:
#         stats = PasswordStats(password)
#         strength = stats.strength()

#         if strength < 0.3:
#             st.warning("❌ Weak Password")
#             color = "red"
#         elif strength < 0.6:
#             st.info("⚠️ Moderate Password")
#             color = "orange"
#         else:
#             st.success("✅ Strong Password")
#             color = "green"

#         st.progress(strength)



import streamlit as st  # type:ignore
from password_strength import PasswordStats  # type:ignore

# ---- Set page layout ----
st.set_page_config(page_title="Password Strength Meter", layout="centered")

# ---- Custom CSS for Glassmorphism & Neon ----
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

    @keyframes slideUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
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

    .stTextInput input:hover {
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.8);
    }

    /* Password Strength Messages */
    .weak {
        color: #ff4b2b !important;
        font-weight: bold;
        animation: slideUp 0.5s ease-in-out;
    }
    .moderate {
        color: #ff9800 !important;
        font-weight: bold;
        animation: slideUp 0.5s ease-in-out;
    }
    .strong {
        color: #00c853 !important;
        font-weight: bold;
        animation: slideUp 0.5s ease-in-out;
    }

    /* Progress Bar with Gradient */
    .stProgress > div > div > div {
        border-radius: 12px;
        background: linear-gradient(270deg, #00c9ff, #92fe9d);
        transition: all 0.5s ease-in-out;
        animation: zoomIn 0.6s ease-in-out;
    }

    @keyframes zoomIn {
        from { transform: scale(0.8); opacity: 0; }
        to { transform: scale(1); opacity: 1; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- Create a centered container ----
with st.container():
    st.markdown('<div class="glass-container">', unsafe_allow_html=True)
    st.title("🔮 Password Strength Meter")

    # Password input
    password = st.text_input("Enter your password", type="password", placeholder="Type your password...")

    # Strength calculation
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

        # Apply custom progress bar color dynamically
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
