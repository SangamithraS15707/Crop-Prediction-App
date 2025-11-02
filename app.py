import streamlit as st
import joblib
import numpy as np


# ---- Load the trained model ----
model = joblib.load('random_forest_model.joblib')  # replace with your file path

# ---- Set page config ----
st.set_page_config(
    page_title="Crop Prediction App",
    layout="centered",
    initial_sidebar_state="expanded"
)





st.title("🌱 Crop Prediction App")
st.write("Enter the details below to predict the suitable crop:")

# ---- Input sliders ----
N = st.number_input("Nitrogen content (N)", min_value=0, max_value=140, value=50)
P = st.number_input("Phosphorus content (P)", min_value=0, max_value=140, value=50)
K = st.number_input("Potassium content (K)", min_value=0, max_value=140, value=50)
temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=25.0)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=50.0)
ph = st.number_input("pH value of soil", min_value=0.0, max_value=14.0, value=6.5)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=100.0)

# ---- Prediction ----
if st.button("Predict Crop"):
    # Create input array
    input_features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_features)[0]  # get predicted crop
    st.success(f"🌾 The recommended crop is: **{prediction}**")
