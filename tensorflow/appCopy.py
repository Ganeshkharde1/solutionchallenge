import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step 1: Load the data
data = pd.read_csv('data.csv')  # Update 'your_data.csv' with the actual file name

# Step 2: Preprocess the data
X = data[['rice', 'roti', 'daal', 'sweet']]
y = data['benificries']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 3: Define and train the regression model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Step 4: Evaluate the model
y_pred = model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Step 5: Save the model using pickle
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
