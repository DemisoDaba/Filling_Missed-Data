# -*- coding: utf-8 -*-
"""
Created on Mon Jul 02 17:05:41 2023

@author: Demiso
"""

import tkinter as tk
from tkinter import filedialog
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import os

def fill_missing_data(data_file):
    # Load the data from the CSV file
    data = pd.read_csv(data_file)

    performance = []  # List to store performance values

    # Iterate over the columns and fill missing values using regression
    for col in data.columns:
        if data[col].dtype != float:  # Check if the column type is non-numeric
            data[col] = data[col].replace(' ', float('nan'))  # Replace non-numeric values with NaN

        if data[col].isnull().sum() > 0:
            # Separate the feature variables (X) and the target variable (y)
            X_train = data[data[col].notnull()].drop(col, axis=1)
            y_train = data[data[col].notnull()][col]
            X_test = data[data[col].isnull()].drop(col, axis=1)

            # Create an imputer object with the mean strategy
            imputer = SimpleImputer(strategy='mean')

            # Fit and transform the data with mean imputation
            X_train_imputed = imputer.fit_transform(X_train)
            X_test_imputed = imputer.transform(X_test)

            # Create a linear regression model
            model = LinearRegression()

            # Fit the model
            model.fit(X_train_imputed, y_train)

            # Predict the missing values
            y_pred = model.predict(X_test_imputed)

            # Fill the missing values in the column
            data.loc[data[col].isnull(), col] = y_pred

            # Calculate R-squared and store in performance list
            r_squared = r2_score(y_train, model.predict(X_train_imputed))
            performance.append((col, r_squared))

    # Print the filled data
    print("Filled data:")
    print(data)

    # Save the filled data in the same folder as the input data
    output_file = os.path.splitext(data_file)[0] + "_filled.csv"
    data.to_csv(output_file, index=False)
    print("Filled data saved to:", output_file)

    # Display performance metrics in GUI
    performance_label.config(text="Performance R-Squared:")
    for i, (col, r_squared) in enumerate(performance):
        result_label = tk.Label(window, text=f"{col}: {r_squared:.4f}")
        result_label.pack()

def browse_file():
    # Open a file dialog to select the CSV file
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

    # Display the selected file path in the entry field
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def fill_missing_data_gui():
    # Get the selected file path from the entry field
    file_path = file_entry.get()

    # Fill missing data using the selected file
    fill_missing_data(file_path)

# Create the main window
window = tk.Tk()
window.title("Fill Stream-Flow: Regression")

# Create a label and entry field for file selection
file_label = tk.Label(window, text="Select CSV file: ")
file_label.pack()

file_entry = tk.Entry(window, width=50)
file_entry.pack()

# Create a button to browse and select the CSV file
browse_button = tk.Button(window, text="Browse", command=browse_file)
browse_button.pack()

# Create a button to fill missing data
fill_button = tk.Button(window, text="Fill Missing Data", command=fill_missing_data_gui)
fill_button.pack()

# Create a label to display performance metrics
performance_label = tk.Label(window, text="")
performance_label.pack()

# Start the Tkinter event loop
window.mainloop()
