# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 22:31:18 2023

@author: Demiso
"""

import os
import tkinter as tk
from tkinter import filedialog, font
import numpy as np

# Function to fill missing values using Arithmetic Mean
def fill_missing_data(data):
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

def handle_button_click(method):
    if method == "Arithmetic Mean":
        filled_data = fill_missing_data(data)
        print("Filled Data:")
        print(filled_data)

        # Save filled data in 'filled' folder with the name "filled_data_Arithmetic"
        filled_folder = os.path.join(os.path.dirname(file_path), "filled")
        os.makedirs(filled_folder, exist_ok=True)
        filled_file_path = os.path.join(filled_folder, "filled_data_Arithmetic.csv")
        np.savetxt(filled_file_path, filled_data, delimiter=",", fmt="%.5f", header=','.join(column_names), comments='')
        print("Filled data saved successfully.")

def load_data():
    global file_path, column_names
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

button_load_data = tk.Button(frame, text="Load Data", command=load_data)
button_load_data.pack(side=tk.LEFT)

label_data_location = tk.Label(window, text="Data Location: ")
label_data_location.pack()

window.mainloop()
