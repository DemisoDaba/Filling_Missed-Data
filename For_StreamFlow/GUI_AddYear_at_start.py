# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 11:47:36 2023

@author: Demiso
"""

import tkinter as tk
from tkinter import filedialog
import pandas as pd

def load_data():
    global df
    # Open a file dialog to select the input CSV file
    input_file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    if input_file_path:
        # Read the input CSV file into a DataFrame
        df = pd.read_csv(input_file_path)
        status_label.config(text="Data loaded successfully!")

def calculate_year():
    if 'df' not in globals():
        status_label.config(text="Please load data first.")
        return

    # Get the starting year from the input field
    starting_year = int(starting_year_entry.get())

    # Initialize variables for year
    current_year = starting_year

    # List to store year values for each row
    years = []

    # Iterate through the DataFrame and calculate the year based on the day
    for _, row in df.iterrows():
        day = row['Date']
        
        # Check if the day is 1, indicating the start of a new year
        if day == 1:
            current_year += 1
        
        years.append(current_year)

    # Add the calculated "Year" column to the DataFrame
    df.insert(0, 'Year', years)  # Insert "Year" column at the beginning

    # Save the modified DataFrame to a new CSV file
    output_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if output_file_path:
        df.to_csv(output_file_path, index=False)
        status_label.config(text=f"Year column added and saved to {output_file_path}")

# Create the main application window
app = tk.Tk()
app.title("Year Calculation")

# Create and place widgets
starting_year_label = tk.Label(app, text="Starting Year:")
starting_year_label.pack()

starting_year_entry = tk.Entry(app)
starting_year_entry.pack()

load_data_button = tk.Button(app, text="Load Data", command=load_data)
load_data_button.pack()

calculate_button = tk.Button(app, text="Calculate", command=calculate_year)
calculate_button.pack()

status_label = tk.Label(app, text="")
status_label.pack()

app.mainloop()
