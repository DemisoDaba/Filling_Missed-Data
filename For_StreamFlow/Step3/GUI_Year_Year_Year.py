# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 12:07:31 2023

@author: Demiso
"""

import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os

# Function to rearrange data and save with a meaningful name
def rearrange_and_save_data():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        # Load your data from the selected CSV file
        df = pd.read_csv(file_path)

        # Replace the "AbayNear_output" column with the fourth column (assuming it's the default fourth column)
        df['AbayNear_output'] = df.iloc[:, 3]

        # Create a new DataFrame to store the rearranged data
        rearranged_df = pd.DataFrame(columns=df['Year'].unique())

        # Iterate through the unique years and arrange the values
        for year in df['Year'].unique():
            values = df[df['Year'] == year]['AbayNear_output'].reset_index(drop=True)
            rearranged_df[year] = values

        # Extract the file name (without extension) from the input file path
        file_name = os.path.splitext(os.path.basename(file_path))[0]

        # Construct the output file path with the meaningful word
        output_file_path = f"{file_name}_formatted.csv"

        # Export the rearranged data to the new CSV file
        rearranged_df.to_csv(output_file_path, index=False)

        print(f"Data exported to '{output_file_path}'")

# Create the main application window
root = tk.Tk()
root.title("Data Rearrangement with GUI")

# Create a button to load data, rearrange, and save
rearrange_button = tk.Button(root, text="Load, Rearrange, and Save Data", command=rearrange_and_save_data)
rearrange_button.pack()

# Start the GUI application
root.mainloop()
