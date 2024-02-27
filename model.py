
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


