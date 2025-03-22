import streamlit as st
import numpy as np
import joblib

# 1. Load the Model
model = joblib.load("rf_model.pkl")

st.title("Laptop Price Prediction")

st.divider()

st.write("Welcome to the Laptop Price Prediction App! This application is designed to provide you with an estimated price for a laptop based on its specifications. As a financial service, we often handle laptops as collateral. This tool can serve as a valuable estimator for determining laptop value in our operations.")

st.divider() 

st.write("Please enter the laptop's details below:")

Processor_Speed = st.number_input("Enter Processor Speed", value = 2.50, step=0.50)
RAM_Size = st.number_input("Enter RAM Size", value=16, step=8)
Storage_Capacity = st.number_input("Enter Storage Capacity", value=512, step =256)

x = [Processor_Speed, RAM_Size, Storage_Capacity]

st.divider()

prediction = st.button("Click to Estimate laptop Price")

st.divider()

if prediction:
        
        st.balloons()

        x1 = np.array(x)

        prediction = model.predict([x1])[0] # return direct not array

        st.write(f"Price estimation for the laptop is: {prediction:,.2f}")

else:
    st.write("Push the button to estimate laptop price")