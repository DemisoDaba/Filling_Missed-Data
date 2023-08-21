# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 21:30:09 2023

@author: Demiso
"""

import pandas as pd
import calendar
import os

# Read the data from the CSV file
csv_filename = 'Hello.csv'
rainfall_data = pd.read_csv(csv_filename)

# Get the range of years from the data
min_year = int(rainfall_data['Year'].min())  # Convert to integer
max_year = int(rainfall_data['Year'].max())  # Convert to integer

# Initialize lists to store data
all_data = []

# Loop through the years, months, and days
for year in range(min_year, max_year + 1):
    for month in range(1, 13):  # Months from 1 to 12
        days_in_month = calendar.monthrange(year, month)[1]  # Get the number of days in the month
        for day in range(1, days_in_month + 1):
            # Find the corresponding rainfall value
            mask = (rainfall_data['Year'] == year) & (rainfall_data['Month'] == month)
            if mask.any():
                rainfall = rainfall_data.loc[mask, str(day)].values[0]
            else:
                rainfall = ''
            
            all_data.append([year, month, day, rainfall])

# Create a DataFrame from the list
result_df = pd.DataFrame(all_data, columns=['Year', 'Month', 'Day', 'Rainfall'])

# Derive the new filename
output_filename = os.path.splitext(csv_filename)[0] + '_vertical_rainfall_with_dates.csv'

# Save the DataFrame to a CSV file
result_df.to_csv(output_filename, index=False)

print(f"Vertical rainfall values with dates saved to '{output_filename}'")
