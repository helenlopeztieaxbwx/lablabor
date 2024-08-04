# Initialize the hourly solar radiation value (measured in kWh/m^2)
hourly_solar_radiation = 1  # This is the input measured value for one hour

# Number of hours in a day
hours_in_day = 24

# Calculate the total solar radiation for the day
total_daily_solar_radiation = hourly_solar_radiation * hours_in_day

# Print the result
print(f"Total daily solar radiation: {total_daily_solar_radiation} kWh/m^2")
