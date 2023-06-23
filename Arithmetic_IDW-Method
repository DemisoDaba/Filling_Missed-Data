# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 08:13:45 2023
@author: Demiso
"""

import os
import tkinter as tk
from tkinter import filedialog, font
import numpy as np
from os.path import join

coordinates = None  # Initialize the coordinates variable

# Function to fill missing values using Arithmetic Mean
def fill_missing_data_arithmetic(data):
    filled_data = np.copy(data)  # Create a copy of the data to avoid modifying the original array

    num_stations = data.shape[1]  # Get the number of stations
    num_days = data.shape[0]  # Get the number of days

    # Iterate over each station
    for station in range(num_stations):
        # Iterate over each day
        for day in range(num_days):
            if np.isnan(data[day, station]):
                # Find neighboring stations that have valid data
                neighboring_stations = []
                for neighbor in range(num_stations):
                    if neighbor != station and not np.isnan(data[day, neighbor]):
                        neighboring_stations.append(neighbor)

                if neighboring_stations:
                    # Calculate the mean of neighboring stations' data
                    mean_value = np.nanmean(data[day, neighboring_stations])
                    filled_data[day, station] = mean_value

    return filled_data

# Function to fill missing values using Inverse Distance Weighting
def fill_missing_data_inverse_distance(data, coordinates):
    filled_data = np.copy(data)  # Create a copy of the data to avoid modifying the original array

    num_stations = data.shape[1]  # Get the number of stations
    num_days = data.shape[0]  # Get the number of days

    # Iterate over each station
    for station in range(num_stations):
        # Iterate over each day
        for day in range(num_days):
            if np.isnan(data[day, station]):
                # Find neighboring stations that have valid data
                neighboring_stations = []
                for neighbor in range(num_stations):
                    if neighbor != station and not np.isnan(data[day, neighbor]):
                        neighboring_stations.append(neighbor)

                if neighboring_stations:
                    # Calculate the inverse distance weighted value of neighboring stations' data
                    weighted_sum = 0.0
                    total_weight = 0.0
                    for neighbor in neighboring_stations:
                        distance = abs(station - neighbor)
                        weight = 1.0 / distance
                        weighted_sum += data[day, neighbor] * weight
                        total_weight += weight

                    filled_data[day, station] = weighted_sum / total_weight

    return filled_data

def handle_button_click(method):
    if method == "Arithmetic Mean":
        filled_data = fill_missing_data_arithmetic(data)
        print("Filled Data using Arithmetic Mean:")
        print(filled_data)

        # Save filled data in 'filled' folder with the name "filled_data_Arithmetic"
        filled_folder = os.path.join(os.path.dirname(file_path), "filled")
        os.makedirs(filled_folder, exist_ok=True)
        filled_file_path = join(filled_folder, "filled_data_Arithmetic.csv")
        np.savetxt(filled_file_path, filled_data, delimiter=",", fmt="%.5f", header=','.join(column_names), comments='')
        print("Filled data saved successfully.")
    elif method == "Inverse Distance Weighting":
        if coordinates is None:
            print("Error: Coordinates not loaded.")
            return

        filled_data = fill_missing_data_inverse_distance(data, coordinates)
        print("Filled Data using Inverse Distance Weighting:")
        print(filled_data)

        # Save filled data in 'filled' folder with the name "filled_data_InverseDistance.csv"
        filled_folder = os.path.join(os.path.dirname(file_path), "filled")
        os.makedirs(filled_folder, exist_ok=True)
        filled_file_path = join(filled_folder, "filled_data_InverseDistance.csv")
        np.savetxt(filled_file_path, filled_data, delimiter=",", fmt="%.5f", header=','.join(column_names), comments='')
        print("Filled data saved successfully.")
    else:
        print("Invalid fill method.")

def load_coordinates():
    global coordinates, coordinates_file_path
    coordinates_file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("CSV files", "*.csv")])
    if coordinates_file_path:
        try:
            coordinates_data = np.genfromtxt(coordinates_file_path, delimiter=",", skip_header=1, dtype=str)

            # Validate the loaded coordinates data
            if len(coordinates_data.shape) != 2 or coordinates_data.shape[1] < 3:
                raise ValueError("Invalid coordinates file format.")

            station_names = coordinates_data[:, 0]
            x_coordinates = coordinates_data[:, 1]
            y_coordinates = coordinates_data[:, 2]

            if any(station_name == "" or station_name is None for station_name in station_names):
                raise ValueError("Missing or empty station names in the coordinates file.")
            if any(x_coord == "" or x_coord is None for x_coord in x_coordinates):
                raise ValueError("Missing or empty X coordinates in the coordinates file.")
            if any(y_coord == "" or y_coord is None for y_coord in y_coordinates):
                raise ValueError("Missing or empty Y coordinates in the coordinates file.")

            coordinates = coordinates_data[:, 1:3]
            print("Coordinates loaded successfully.")
            label_coordinates_location.config(text="Coordinates Location: " + coordinates_file_path)
        except Exception as e:
            print("Error loading coordinates:", str(e))
def load_data():
    global file_path, column_names, coordinates
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("CSV files", "*.csv")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                column_names = file.readline().strip().split(',')

            global data
            data = np.genfromtxt(file_path, delimiter=",", skip_header=1, missing_values="", filling_values=np.nan)
            print("Data loaded successfully.")
            label_data_location.config(text="Data Location: " + file_path)
        except Exception as e:
            print("Error loading data:", str(e))

window = tk.Tk()
window.title("Filling")

frame = tk.Frame(window)
frame.pack()

bold_font = font.Font(weight="bold")
label_rainfall = tk.Label(frame, text="For Rainfall", font=bold_font, fg="black", bg="sky blue")
label_rainfall.pack(side=tk.TOP, fill=tk.X)

label_title = tk.Label(frame, text="Methods", fg="green", bg="yellow")
label_title.pack(side=tk.LEFT)

button_arithmetic_mean = tk.Button(frame, text="Arithmetic Mean", command=lambda: handle_button_click("Arithmetic Mean"))
button_arithmetic_mean.pack(side=tk.LEFT)

button_inverse_distance_weighting = tk.Button(frame, text="Inverse Distance W", command=lambda: handle_button_click("Inverse Distance Weighting"))
button_inverse_distance_weighting.pack(side=tk.LEFT)

button_load_data = tk.Button(frame, text="Load Data", command=load_data)
button_load_data.pack(side=tk.LEFT)

button_load_coordinates = tk.Button(frame, text="Load Coordinates", command=load_coordinates)
button_load_coordinates.pack(side=tk.LEFT)

label_data_location = tk.Label(window, text="Data Location: ")
label_data_location.pack()

label_coordinates_location = tk.Label(window, text="Coordinates Location: ")
label_coordinates_location.pack()

window.mainloop()
