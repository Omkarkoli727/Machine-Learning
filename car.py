import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

st.title("Car Price Prediction Dashboard")

present_price = st.number_input("Present Price (Lakhs)", min_value=0.0, value=5.0)
kms_driven = st.number_input("Kilometers Driven", min_value=0, value=30000)

fuel_type = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG"]
)

seller_type = st.selectbox(
    "Seller Type",
    ["Dealer", "Individual"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

owner = st.selectbox(
    "Number of Previous Owners",
    [0, 1, 2, 3]
)

car_age = st.slider(
    "Car Age",
    0,
    20,
    5
)

if st.button("Predict Price"):

    user_data = pd.DataFrame({
        "Present_Price": [present_price],
        "Kms_Driven": [kms_driven],
        "Fuel_Type": [fuel_type],
        "Seller_Type": [seller_type],
        "Transmission": [transmission],
        "Owner": [owner],
        "Car_Age": [car_age]
    })

    model = joblib.load("model\car_price_model.pkl")

    prediction = model.predict(user_data)[0]

    st.success(
        f"Estimated Selling Price: ₹ {prediction:.2f} Lakhs"
    )

    chart_df = pd.DataFrame({
        "Category": ["Predicted Price"],
        "Value": [prediction]
    })

    fig = px.bar(
        chart_df,
        x="Category",
        y="Value",
        title="Predicted Car Price"
    )

    st.plotly_chart(fig, use_container_width=True)