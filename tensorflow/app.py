import streamlit as st
import numpy as np
import pickle

# Load the pickled model
with open('model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Function to make predictions
def predict_beneficiaries(rice, roti, daal, sweet):
    input_data = np.array([[rice, roti, daal, sweet]])
    prediction = loaded_model.predict(input_data)
    return prediction[0]

# Streamlit UI

# st.image("img.png")
st.columns(3)[1].image("img.png")
st.title('No. of Beneficiaries Prediction App')

st.header('Input Parameters')
rice = st.slider('Rice Quantity', min_value=0, max_value=100)
roti = st.slider('Roti Quantity', min_value=0, max_value=100)
daal = st.slider('Daal Quantity', min_value=0, max_value=100)
sweet = st.slider('Sweet Quantity', min_value=0, max_value=100)

if st.button('Predict'):
    prediction = predict_beneficiaries(rice, roti, daal, sweet)
    st.success(f'Predicted number of beneficiaries: {prediction:.2f}')
