import numpy as np
import pandas as pd
from scipy.signal import savgol_filter
from collections import deque
import time

# Load data and filter to start from 0.32 seconds
file_path = '240915_0907'  # Ensure this file is in the same directory as the code
data = pd.read_csv(file_path, delimiter='\t')
filtered_data = data[data['Time'] >= 0.32].reset_index(drop=True)

# Parameters
SAMPLING_RATE = 50  # Hz
DT = 1.0 / SAMPLING_RATE  # Time step in seconds
WINDOW_LENGTH = 5  # Savitzky-Golay filter window length (must be odd)
POLYORDER = 2  # Polynomial order for Savitzky-Golay filter
LAG_ORDER = 1  # VAR model lag order
BUFFER_SIZE = 20  # Number of past observations to keep

# Initialize buffers and series lists
torque_buffer = deque(maxlen=BUFFER_SIZE)
angle_buffer = deque(maxlen=BUFFER_SIZE)
velocity_buffer = deque(maxlen=BUFFER_SIZE)

torque_series = []
angle_series = []
velocity_series = []

# Function to predict the next torque using a VAR(1) model
def predict_next_torque(torque_series, angle_series, velocity_series):
    if len(torque_series) < LAG_ORDER + 1:
        return torque_series[-1]
    else:
        Y = np.array(torque_series[LAG_ORDER:])
        X = np.column_stack([
            np.ones(len(Y)),  # Intercept term
            np.array(torque_series[:-LAG_ORDER]),
            np.array(angle_series[:-LAG_ORDER]),
            np.array(velocity_series[:-LAG_ORDER])
        ])
        coeffs, _, _, _ = np.linalg.lstsq(X, Y, rcond=None)
        last_X = np.array([1, torque_series[-1], angle_series[-1], velocity_series[-1]])
        return np.dot(last_X, coeffs)

# Measure the time taken to run the loop
start_time = time.time()

# Simulated loop over the dataset for real-time prediction
predictions = []
for index, row in filtered_data.iterrows():
    current_torque = row['T_a']
    current_angle = row['ElbowAngle']
    current_velocity = row['ElbowJointVelocity']

    torque_buffer.append(current_torque)
    angle_buffer.append(current_angle)
    velocity_buffer.append(current_velocity)

    if len(torque_buffer) >= WINDOW_LENGTH:
        torque_smoothed = savgol_filter(list(torque_buffer), WINDOW_LENGTH, POLYORDER)
        angle_smoothed = savgol_filter(list(angle_buffer), WINDOW_LENGTH, POLYORDER)
        velocity_smoothed = savgol_filter(list(velocity_buffer), WINDOW_LENGTH, POLYORDER)
    else:
        torque_smoothed = list(torque_buffer)
        angle_smoothed = list(angle_buffer)
        velocity_smoothed = list(velocity_buffer)

    torque_series.append(torque_smoothed[-1])
    angle_series.append(angle_smoothed[-1])
    velocity_series.append(velocity_smoothed[-1])

    if len(torque_series) >= LAG_ORDER + 1:
        next_torque_pred = predict_next_torque(torque_series, angle_series, velocity_series)
    else:
        next_torque_pred = torque_series[-1]

    predictions.append(next_torque_pred)

# Calculate the percentage error for each timestep
filtered_data['Predicted_T_a'] = predictions
filtered_data['Percentage_Error'] = np.abs((filtered_data['T_a'] - filtered_data['Predicted_T_a']) / filtered_data['T_a']) * 100

# Count the total number of timesteps and those where percentage error > 20%
total_timesteps = len(filtered_data)
high_error_count = (filtered_data['Percentage_Error'] > 20).sum()

# Measure the time taken
end_time = time.time()
execution_time = end_time - start_time

# Print results
print(f"Total number of timesteps: {total_timesteps}")
print(f"Number of timesteps with percentage error > 20%: {high_error_count}")
print(f"Time taken to execute the code: {execution_time:.6f} seconds")
