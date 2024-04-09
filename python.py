import joblib
import pandas as pd
import streamlit as st

def show_entry_fields():
    p1 = float(e1)
    p2 = float(e2)
    p3 = float(e3)
    p4 = float(e4)
    p5 = float(e5)
    p6 = float(e6)
    p7 = float(e7)
    
    model = joblib.load('car_price_predictor')
    data_new = pd.DataFrame({
        'Present_Price': p1,
        'Kms_Driven': p2,
        'Fuel_Type': p3,
        'Seller_Type': p4,
        'Transmission': p5,
        'Owner': p6,
        'Age': p7
    }, index=[0])
    
    result = model.predict(data_new)
    st.text("Car Purchase amount")
    st.text(result[0])
    print("Car Purchase amount", result[0])

st.title("Car Price Prediction Using Machine Learning")

# st.text("Present_Price")
# st.text("Kms_Driven")
# st.text("Fuel_Type")
# st.text("Seller_Type")
# st.text("Transmission")
# st.text("Owner")
# st.text("Age")

e1 = st.number_input("Present_Price")
e2 = st.number_input("Kms_Driven")
e3 = st.number_input("Fuel_Type")
e4 = st.number_input("Seller_Type")
e5 = st.number_input("Transmission")
e6 = st.number_input("Owner")
e7 = st.number_input("Age")

if st.button('Predict'):
    show_entry_fields()
