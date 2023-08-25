import tkinter as tk
from tkinter import filedialog
from tkinter import font
import pandas as pd
import numpy as np
import os

def convert_to_nan(value):
    try:
        return float(value)
    except:
        return np.nan

def rearrange_data():
    csv_filename = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV files", "*.csv")])

    if csv_filename:
        df = pd.read_csv(csv_filename)
        df = pd.read_csv(csv_filename, converters={col: convert_to_nan for col in df.columns})
        base_filename = os.path.splitext(os.path.basename(csv_filename))[0]
        df["Year"] = df["Year"].astype(int)
        
        rearranged_df = pd.DataFrame(columns=["Year", "Month", "Dates", base_filename])
        
        for year in df["Year"].unique():
            year_data = df[df["Year"] == year]
            for month in df.columns[2:]:
                month_name = month
                month_data = year_data[["Dates", month]].rename(columns={month: base_filename})
                month_data.insert(0, "Month", month_name)
                month_data.insert(0, "Year", year)
                rearranged_df = pd.concat([rearranged_df, month_data], ignore_index=True)
        
        rearranged_csv_filename = f'Rearranged_{base_filename}.csv'
        rearranged_df.to_csv(rearranged_csv_filename, index=False)
        result_label.config(text=f"Data saved to {rearranged_csv_filename}", fg="blue")

# Create the main application window
app = tk.Tk()
app.title("Data Rearrangement Tool")  # Set the title

# Create a bold font
bold_font = font.Font(weight="bold")

# Create a label for the title
title_label = tk.Label(app, text="Data Rearrangement Tool", fg="black", bg="sky blue")
title_label.grid(row=0, columnspan=2, pady=10)

# Create a label for Select .csv file with green background
select_label = tk.Label(app, text="Select .csv file & perform task",fg="green", bg="yellow")
select_label.grid(row=1, column=0, padx=5)

# Create a button for Load Data
load_button = tk.Button(app, text="Load Data & VLook_Up", command=rearrange_data)
load_button.grid(row=1, column=1, padx=5)

# Create a label to display the result
result_label = tk.Label(app, text="", font=("Helvetica", 12))
result_label.grid(row=3, columnspan=2)

# Start the GUI event loop
app.mainloop()
