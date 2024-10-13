import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from sklearn.metrics import mean_squared_error, r2_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, BatchNormalization, Dropout, LeakyReLU, PReLU, ReLU
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l2
import shap

# Load the data
try:
    file_path = "C:/Users/arago/Documents/Study/Projects/OCP/DATA_fealtred_cleaned.xlsx"
    data = pd.read_excel(file_path)
except Exception as e:
    print(f"Error loading data: {e}")
    raise

# Define features and target variable
x = data[['Ds', 'VTs', 'TE_1er','TS_1er','TE_2eme','TS_2eme','TE_3eme','TS_3eme','TE_4eme','TS_4eme']] 
y = data['SO2_chemine'] 

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)

# Build the model with additional layers and adjusted activation functions
def build_model(input_shape):
    model = Sequential([
        Dense(512, activation='relu', kernel_regularizer=l2(0.00005)),
        BatchNormalization(),
        Dropout(0.3),

        Dense(256, activation='relu', kernel_regularizer=l2(0.00005)),
        BatchNormalization(),
        Dropout(0.3),

        Dense(128, activation='relu', kernel_regularizer=l2(0.00005)),
        BatchNormalization(),
        Dropout(0.3),

        Dense(64, activation='relu', kernel_regularizer=l2(0.00005)),
        BatchNormalization(),
        Dropout(0.3),

        Dense(32, kernel_regularizer=l2(0.00005)),
        LeakyReLU(alpha=0.01),
        BatchNormalization(),
        Dropout(0.3),

        Dense(16, kernel_regularizer=l2(0.00005)),
        LeakyReLU(alpha=0.01),

        Dense(8, kernel_regularizer=l2(0.00005)),
        PReLU(),

        Dense(4, kernel_regularizer=l2(0.00005)),
        ReLU(),

        Dense(1, activation='linear')
    ])
    return model

# Initialize and compile the model
model = build_model(X_train.shape[1])

optimizer = Adam(learning_rate=0.001)
model.compile(optimizer=optimizer, loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=2000, batch_size=64, validation_data=(X_val, y_val))

y_pred = model.predict(X_train)

# Reshape y_pred if necessary (especially if using a single output neuron)
if y_pred.shape != y_val.shape:
    y_pred = y_pred.reshape(-1)

# Calculate Mean Squared Error and R² score
mse = mean_squared_error(y_train, y_pred)
print(f"Mean Squared Error on validation set: {mse}")

r2 = r2_score(y_train, y_pred)
print(f"R² score on validation set: {r2}")
print(y_pred)

def evaluate_model(model, X, y):
    predictions = model.predict(X)
    return mean_squared_error(y, predictions)

baseline_performance = evaluate_model(model, X_train, y_train)

def permutation_importance(model, X, y, baseline_performance):
    feature_importance = []
    for i in range(X.shape[1]):
        X_permuted = X.copy()
        np.random.shuffle(X_permuted[:, i])
        permuted_performance = evaluate_model(model, X_permuted, y)
        importance = permuted_performance - baseline_performance
        feature_importance.append(importance)
    return feature_importance

baseline_performance = evaluate_model(model, X_train, y_train)

feature_names = x.columns.values
feature_importance = permutation_importance(model, X_train, y_train, baseline_performance)

importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': feature_importance})
importance_df = importance_df.sort_values(by='Importance', ascending=False)

output_file_path = "feature_importance.xlsx"
try:
    importance_df.to_excel(output_file_path, index=False)
    print(f"Feature importance exported to {output_file_path}")
except Exception as e:
    print(f"Error exporting feature importance: {e}")
