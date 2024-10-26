import streamlit as st
import joblib
import numpy as np

# Load the trained Gradient Boosting model from the specified path
model = joblib.load('D:\.intel\Ds\Capstone3\Project/tuned_gradient_boosting_model.pkl')

# Title of the application
st.title("Car Price Prediction App")

# Instructions for the user
st.write("""
### Enter the car features below to predict the price.
""")

# Input features for the car price prediction
# Each feature is represented as a slider or dropdown for user input
width = st.slider('Width (mm)', min_value=1600, max_value=2000, value=1700)
wheel_size = st.slider('Wheel Size (inches)', min_value=14, max_value=22, value=16)
alloy_wheel_size = st.slider('Alloy Wheel Size (inches)', min_value=14, max_value=22, value=16)
model_year = st.slider('Model Year', min_value=2000, max_value=2024, value=2015)
max_power = st.slider('Max Power (hp)', min_value=50, max_value=500, value=150)
length = st.slider('Length (mm)', min_value=3500, max_value=5000, value=4000)
km = st.slider('Mileage (km)', min_value=0, max_value=200000, value=50000)
city = st.selectbox('City', ['Chennai', 'Kolkata', 'Bangalore', 'Hyderabad', 'Jaipur', 'Delhi'])
engine_type = st.selectbox('Engine Type', ['Petrol', 'Diesel', 'Electric', 'LPG', 'CNG'])

acceleration = st.slider('Acceleration (0-100 km/h in seconds)', min_value=2.0, max_value=20.0, value=10.0)
wheel_base = st.slider('Wheel Base (mm)', min_value=2000, max_value=4000, value=2700)
kerb_weight = st.slider('Kerb Weight (kg)', min_value=500, max_value=3000, value=1500)
torque = st.slider('Torque (Nm)', min_value=50, max_value=1000, value=200)
mileage = st.slider('Mileage (km/l)', min_value=5.0, max_value=30.0, value=15.0)
displacement = st.slider('Displacement (cc)', min_value=800, max_value=5000, value=2000)

# Convert categorical features (engine type and city) to numerical values for model input
engine_type_map = {'Petrol': 1, 'Diesel': 0, 'Electric': 2, 'LPG': 3, 'CNG': 4}
engine_type_num = engine_type_map.get(engine_type, -1)  # Default to -1 if engine type not found

# Convert city to a numerical value
city_map = {'Chennai': 0, 'Kolkata': 1, 'Bangalore': 2, 'Hyderabad': 3, 'Jaipur': 4, 'Delhi': 5}
city_num = city_map.get(city, -1)  # Default to -1 if city not found

# Prepare the input data as an array with 15 features for prediction
input_data = np.array([[
    width, wheel_size, alloy_wheel_size, model_year, max_power, 
    length, km, engine_type_num, acceleration, wheel_base, 
    kerb_weight, torque, mileage, displacement, city_num
]])

# Predict button to trigger the prediction
if st.button('Predict Price'):
    try:
        # Make the prediction using the loaded model
        predicted_price = model.predict(input_data)[0]

        # Display the predicted price result to the user
        st.success(f"The estimated car price is: ₹{predicted_price:,.2f}")
    except Exception as e:
        # Display an error message if prediction fails
        st.error(f"An error occurred: {str(e)}")
