
import streamlit as st
import pickle
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the pre-trained model
model_path = "models/LRmodel.pkl"  # Make sure you have a pre-trained model
with open(model_path, "rb") as file:
    model = pickle.load(file)
# Page Configuration


st.set_page_config(page_title="Real Estate Price Prediction", layout="centered")
st.markdown("""
    <style>
        /* Custom Background */
        body {
            background: linear-gradient(135deg, #f0f4f8, #c2c7d0);
            font-family: 'Arial', sans-serif;
        }
        
        .title {
            color: #1f77b4;
            text-align: center;
            font-size: 2.5em;
            font-weight: bold;
            margin-top: 20px;
        }

        .subheader {
            text-align: center;
            color: #333;
            font-size: 1.5em;
        }

        .input-container {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 30px;
        }

        .input-label {
            font-weight: bold;
            color: #1f77b4;
        }

        .stButton button {
            background-color: #1f77b4;
            color: white;
            padding: 12px 24px;
            font-size: 1.1em;
            border-radius: 5px;
            border: none;
        }

        .stButton button:hover {
            background-color: #155a8a;
        }

        .result-text {
            font-size: 1.2em;
            color: #28a745;
            text-align: center;
            margin-top: 20px;
        }

        .image-container {
            text-align: center;
            margin-top: 30px;
        }

        .image-container img {
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        
        .stTextInput, .stNumberInput, .stSelectbox, .stTextArea {
        background-color: #f5f5f5;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 10px;
        font-size: 14px;
        color: #333;
    }
    .stTextInput:hover, .stNumberInput:hover, .stSelectbox:hover, .stTextArea:hover {
        border-color: #1f77b4;
    }
    .stSelectbox select, .stNumberInput input {
        background-color: #ffffff;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# Application title
# Custom title section with blue background
st.markdown(
    """
    <div style="background-color:#1f77b4;padding:20px;border-radius:10px">
    <h1 style="color:white;text-align:center;">Real Estate Price Prediction</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Description
st.markdown(
    """
    <p style="font-size:16px;color:#333;text-align:center;margin-top:10px;">
    This application predicts the price of a property based on its characteristics.
    </p>
    """,
    unsafe_allow_html=True
)



# Property features input form
with st.form("property_inputs"):
   
    st.subheader("Property Details")
    # Create columns for the form
    col1, col2= st.columns(2)
    with col1:
        year_built = st.number_input("Year Built", min_value=1800, max_value=2025, step=1, value=2000)
        beds = st.number_input("Number of Bedrooms", min_value=0, step=1, value=2)
        baths = st.number_input("Number of Bathrooms", min_value=0, step=1, value=1)
        sqft = st.number_input("Square Footage", min_value=100, step=10, value=1000)
        lot_size = st.number_input("Lot Size", min_value=0, step=100, value=500)
        basement = st.selectbox("Has Basement", options=["Yes", "No"])

    with col2:
        property_type = st.selectbox("Property Type", options=["Bungalow", "Condo"])
        property_tax = st.number_input("Annual Property Tax", min_value=0, step=10, value=500)
        insurance = st.number_input("Annual Insurance Cost", min_value=0, step=10, value=300)
        year_sold = st.number_input("Year Sold", min_value=1900, max_value=2025, step=1, value=2023)
        popular = st.selectbox("Popular Property", options=["Yes", "No"])
        recession = st.selectbox("Sold During Recession", options=["Yes", "No"])
        
    submitted = st.form_submit_button("Predict Price")


# Data processing and prediction
if submitted:
    basement_value = 1 if basement == "Yes" else 0
    property_type_Bungalow = 1 if property_type == "Bungalow" else 0
    property_type_Condo = 1 if property_type == "Condo" else 0
    popular_value = 1 if popular == "Yes" else 0
    recession_value = 1 if recession == "Yes" else 0
    property_age = year_sold - year_built
    
    # Prepare model input
    input_data = [[year_sold, property_tax, insurance, beds, baths, sqft, year_built,
                   lot_size, basement_value, popular_value, recession_value, property_age,
                   property_type_Bungalow, property_type_Condo]]
    
    # Predict the price
    predicted_price = model.predict(input_data)[0]
    
    # Display the result
    st.markdown(f'<div class="result-text">The estimated property price is **${predicted_price:,.2f}**</div>', unsafe_allow_html=True)
    st.image("market.png", caption="Real Estate Market Trends", use_container_width=True)

# --- Feature explanation ---
st.markdown(
    """
    <div style="background-color:#f0f2f6;padding:10px 20px;border-radius:10px;margin-top:30px">
    <h4 style="color:#1f77b4;"> How does this work?</h4>
    <p style="color:#333;">
   We used a machine learning (Linear Regression) model to predict your estimated property price, the features used in this prediction are ranked by relative
    importance below.
    </p>
    </div>
    """,
    unsafe_allow_html=True
)
