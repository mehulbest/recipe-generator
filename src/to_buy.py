import streamlit as st

# Custom CSS to style the app
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        color: #333;
        font-family: 'Arial', sans-serif;
        background-image: url('https://example.com/background1.png'), url('https://example.com/background2.png');
        background-size: contain, contain;
        background-repeat: no-repeat, no-repeat;
        background-position: top left, bottom right;
        transition: background 0.3s ease-in-out;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 4px;
        padding: 10px 24px;
        cursor: pointer;
        margin-top: 20px;
        transition: background-color 0.3s ease-in-out;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stMarkdown h2 {
        color: #333;
        text-align: center;
        margin-top: 40px;
        font-size: 36px;
        transition: color 0.3s ease-in-out;
    }
    .stMarkdown h2:hover {
        color: #4CAF50;
    }
    footer {
        text-align: center;
        margin-top: 40px;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

# Add a title and description
st.markdown("<h2>🛒 To Buy List 🛒</h2>", unsafe_allow_html=True)

# Display "To Buy" list
if 'to_buy_list' in st.session_state and st.session_state.to_buy_list:
    st.markdown("### Your 'To Buy' List", unsafe_allow_html=True)
    for item in st.session_state.to_buy_list:
        st.write(f"- {item}")

    # Button to clear "To Buy" list
    if st.button('Clear List'):
        st.session_state.to_buy_list = []
        st.success('List cleared')
else:
    st.markdown("Your 'To Buy' list is empty.", unsafe_allow_html=True)

# Navigation back to main page
st.markdown("[Back to Recipe Generator](recipe.py)")

# Add a footer
st.markdown("""
    <hr>
    <footer>
        <p style='text-align: center;'>
            Made with ❤️ by Mehul Uniyal
        </p>
    </footer>
    """, unsafe_allow_html=True)
