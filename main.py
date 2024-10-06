import streamlit as st
import pandas as pd
from prediction_helper import load_model, predict_price

# Load the model from the artifacts folder
model = load_model('artifacts/model.pkl')

# Streamlit app title
st.title("HOUSE PRICE PREDICTION:INDIA")

# User input features
st.header("Enter the details of the house/home")

number_of_bedrooms = st.number_input("Number of Bedrooms", min_value=0)
number_of_bathrooms = st.number_input("Number of Bathrooms", min_value=0)
living_area = st.number_input("Living Area (sq ft)", min_value=0)
lot_area = st.number_input("Lot Area (sq ft)", min_value=0)
built_year = st.number_input("Built Year", min_value=1900, max_value=2024)
number_of_floors = st.number_input("Number of Floors", min_value=1)
grade_of_the_house = st.selectbox("Grade of the House", options=list(range(1, 14)))  # Example grades
number_of_views = st.number_input("Number of Views", min_value=0)
postal_code = st.text_input("Postal Code")
latitude = st.number_input("Latitude")
longitude = st.number_input("Longitude")
living_area_renov = st.number_input("Living Area Renovated (sq ft)", min_value=0)
lot_area_renov = st.number_input("Lot Area Renovated (sq ft)", min_value=0)
area_of_the_house_excluding_basement = st.number_input("Area of the House (excluding Basement) (sq ft)", min_value=0)
area_of_the_basement = st.number_input("Area of the Basement (sq ft)", min_value=0)

# Button to predict
if st.button("Predict Price"):
    features = pd.DataFrame({
        'number_of_bedrooms': [number_of_bedrooms],
        'number_of_bathrooms': [number_of_bathrooms],
        'living_area': [living_area],
        'lot_area': [lot_area],
        'built_year': [built_year],
        'number_of_floors': [number_of_floors],
        'grade_of_the_house': [grade_of_the_house],
        'number_of_views': [number_of_views],
        'postal_code': [postal_code],
        'latitude': [latitude],
        'longitude': [longitude],
        'living_area_renov': [living_area_renov],
        'lot_area_renov': [lot_area_renov],
        'area_of_the_house(excluding_basement)': [area_of_the_house_excluding_basement],
        'area_of_the_basement': [area_of_the_basement]
    })

    # Predict the house price
    predicted_price = predict_price(model, features)
    st.success(f"The predicted house price is: ${predicted_price[0]:,.2f}")
