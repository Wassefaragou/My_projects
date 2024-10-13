import numpy as np
import pandas as p
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
try:
    file_path = "C:/Users/arago/Documents/Study/Projects/OCP/Data.xlsx"
    data = p.read_excel(file_path)
except Exception as e:
    print(f"Error loading data: {e}")
    raise

# Define features and target variable
x = data[['Ds', 'VTs', 'TE_1er', 'TS_1er', 'TE_2eme','TS_2eme','TE_3eme','TS_3eme','TE_4eme','TS_4eme']] 
y = data['SO2_chemine'] 
rf_regressor = RandomForestRegressor(n_estimators=1000, random_state=42)
rf_regressor.fit(x, y)
y_pred = rf_regressor.predict(x)
#%%
mse = mean_squared_error(y, y_pred)
mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)
rmse = np.sqrt(mse)
print(f"Mean Squared Error (MSE): {mse}")
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Root Mean Squared Error (RMSE): {rmse}")
print(f"R-squared (R²): {r2}")