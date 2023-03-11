import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
# Load the saved model
filename = 'linear_regression_model.pkl'
loaded_model = pickle.load(open(filename, 'rb'))

# Define input variables for prediction
input_data = np.array([[65000, 7, 8, 2, 30000]])

# Scale the input variables using the StandardScaler used in training
sc = StandardScaler()
input_data = sc.fit_transform(input_data)

# Make prediction using the loaded model
predicted_price = loaded_model.predict(input_data)

# Print the predicted price
print("The predicted price of the house is: $", predicted_price[0])