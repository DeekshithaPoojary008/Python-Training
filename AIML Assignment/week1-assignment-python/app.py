import streamlit as st
import pandas as pd
import joblib

model = joblib.load("house_model.pkl")

st.title("California House Price Prediction")

income = st.number_input("Median Income")
age = st.number_input("Housing Median Age")
rooms = st.number_input("Total Rooms")
latitude = st.number_input("Latitude")
longitude = st.number_input("Longitude")

if st.button("Predict"):
    data = pd.DataFrame({
        "median_income": [income],
        "housing_median_age": [age],
        "total_rooms": [rooms],
        "latitude": [latitude],
        "longitude": [longitude]
    })

    prediction = model.predict(data)

    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")