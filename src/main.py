import streamlit as st
from streamlit_option_menu import option_menu
from CustomLLM import CustomLLM

llm = CustomLLM()

# Initialize session state for theme if it doesn't exist
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

# Function to switch themes
def switch_theme():
    st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'

# Apply CSS styles based on the selected theme
if st.session_state.theme == 'light':
    st.markdown("""
        <style>
        .main {
            background-color: #f0f2f6;
            color: #000;
            font-family: 'Arial', sans-serif;
            transition: background 0.3s ease-in-out;
        }
        .stTextInput > div > input {
            background-color: #fff;
            border: 1px solid #ccc;
            border-radius: 4px;
            color: #000;
            padding: 10px;
            margin-top: 20px;
            transition: border-color 0.3s ease-in-out;
        }
        .stTextInput > div > input:focus {
            border-color: #4CAF50;
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
            color: #000;
            text-align: center;
            margin-top: 40px;
            font-size: 36px;
            transition: color 0.3s ease-in-out;
        }
        .stMarkdown h2:hover {
            color: #4CAF50;
        }
        .stMarkdown h3 {
            color: #000;
            margin-top: 20px;
        }
        .stSelectbox div[data-baseweb="select"] > div {
            background-color: #fff;
            border: 1px solid #ccc;
            border-radius: 4px;
            color: #000;
            margin-top: 20px;
        }
        .stSelectbox div[data-baseweb="select"] > div:focus {
            border-color: #4CAF50;
        }
        footer {
            text-align: center;
            margin-top: 40px;
            font-size: 16px;
            color: #000;
        }
        .theme-switch-button {
            position: fixed;
            top: 10px;
            right: 10px;
            z-index: 1000;
            padding: 2px 5px;
            font-size: 12px;
            cursor: pointer;
            background-color: #ddd;
            border: none;
            border-radius: 5px;
        }
        .theme-switch-button.light {
            color: #000;
        }
        .theme-switch-button.dark {
            color: #e0e0e0;
            background-color: #333;
        }
        </style>
        """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .main {
            background-color: #1e1e1e;
            color: #e0e0e0;
            font-family: 'Arial', sans-serif;
            transition: background 0.3s ease-in-out;
        }
        .stTextInput > div > input {
            background-color: #2b2b2b;
            border: 1px solid #555;
            border-radius: 4px;
            color: #e0e0e0;
            padding: 10px;
            margin-top: 20px;
            transition: border-color 0.3s ease-in-out;
        }
        .stTextInput > div > input:focus {
            border-color: #4CAF50;
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
            color: #e0e0e0;
            text-align: center;
            margin-top: 40px;
            font-size: 36px;
            transition: color 0.3s ease-in-out;
        }
        .stMarkdown h2:hover {
            color: #4CAF50;
        }
        .stMarkdown h3 {
            color: #e0e0e0;
            margin-top: 20px;
        }
        .stSelectbox div[data-baseweb="select"] > div {
            background-color: #2b2b2b;
            border: 1px solid #555;
            border-radius: 4px;
            color: #e0e0e0;
            margin-top: 20px;
        }
        .stSelectbox div[data-baseweb="select"] > div:focus {
            border-color: #4CAF50;
        }
        footer {
            text-align: center;
            margin-top: 40px;
            font-size: 16px;
            color: #e0e0e0;
        }
        .theme-switch-button {
            position: fixed;
            top: 10px;
            right: 10px;
            z-index: 1000;
            padding: 2px 5px;
            font-size: 12px;
            cursor: pointer;
            background-color: #333;
            color: #e0e0e0;
            border: none;
            border-radius: 5px;
        }
        .theme-switch-button.light {
            color: #333;
        }
        .theme-switch-button.dark {
            color: #e0e0e0;
            background-color: #333;
        }
        </style>
        """, unsafe_allow_html=True)

# Navigation menu
selected_page = option_menu(
    menu_title=None,  # required
    options=["Recipe Generator", "To Buy List"],  # required
    icons=["book", "shopping-cart"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="horizontal",
    
)

# Add the toggle button at the top right of the page
button_label = '🌙' if st.session_state.theme == 'light' else '🌞'

# Add a container to hold the button and manage its state
col1, col2 = st.columns([1, 5])  # Adjust columns to align button to the top right
with col1:
    if st.button(button_label, key='switch_theme', help="Switch theme", use_container_width=False):
        switch_theme()

if selected_page == "Recipe Generator":
    # Recipe Generator Page
    st.markdown("<h2>🍽️ Welcome to the Recipe Generator 🍽️</h2>", unsafe_allow_html=True)
    st.markdown("### Enter a dish name to get the recipe", unsafe_allow_html=True)

    # Input fields for recipe search, dietary preference, and language
    selected_option = st.text_input('Enter a dish name to get the recipe:')
    dietary_options = ['None', 'Vegan', 'Vegetarian', 'Gluten-Free', 'Keto', 'Paleo']
    selected_dietary_option = st.selectbox('Select dietary preference:', dietary_options)
    language = st.selectbox('Select language:', ['English', 'Tamil', 'Spanish', 'French', 'German', 'Italian'])

    if selected_option:
        with st.spinner('Fetching recipe...'):
            # Fetch the recipe with dietary preference and language
            dietary_query = f" {selected_dietary_option}" if selected_dietary_option != 'None' else ""
            recipe = llm(f"give me a {dietary_query} recipe of {selected_option} dish in {language} as output and nothing else")
            ingredients = llm(f"give me the list of ingredients for {selected_option} dish as output and nothing else")
            nutrition_info = llm(f"give me the nutritional information for {selected_option} dish as output and nothing else")

        # Display the recipe and nutritional information
        st.markdown(f"### Recipe for {selected_option} ({selected_dietary_option}) in {language}", unsafe_allow_html=True)
        st.write(recipe)
        st.markdown(f"### Nutritional Information for {selected_option}", unsafe_allow_html=True)
        st.write(nutrition_info)
        st.markdown(f"### Ingredients for {selected_option}", unsafe_allow_html=True)
        st.write(ingredients)

        # Button to add ingredients to "To Buy" list
        if st.button('Add to "To Buy" list'):
            if 'to_buy_list' not in st.session_state:
                st.session_state.to_buy_list = []
            st.session_state.to_buy_list.extend(ingredients.split('\n'))
            st.success('Ingredients added to "To Buy" list.')

if selected_page == "To Buy List":
    # To Buy List Page
    st.markdown("<h2>🛒 Your To Buy List 🛒</h2>", unsafe_allow_html=True)
    
    if 'to_buy_list' in st.session_state and st.session_state.to_buy_list:
        st.markdown("### Your To Buy List:", unsafe_allow_html=True)
        
        # Display each item with a checkbox
        to_buy_list = st.session_state.to_buy_list
        checked_items = []
        for item in to_buy_list:
            if st.checkbox(item, key=item):
                checked_items.append(item)
        
        # Button to clear selected items
        if st.button('Clear Selected Items'):
            st.session_state.to_buy_list = [item for item in to_buy_list if item not in checked_items]
            st.success("Selected items cleared.")
        
        # Button to clear all items
        if st.button('Clear To Buy List'):
            st.session_state.to_buy_list = []
            st.success("To-buy list cleared.")
    else:
        st.write("Your To Buy list is empty.")

# Add a footer to the bottom of every page
st.markdown("""
    <hr>
    <footer>
        <p style='text-align: center;'>
            Made with ❤️ by Mehul Uniyal
        </p>
    </footer>
    """, unsafe_allow_html=True)
