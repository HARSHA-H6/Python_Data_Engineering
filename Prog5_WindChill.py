# Step1: prompt user for Month
month_entered = input("Enter the month number (1 to 12): ")


# Step2: checking if month is digit else setting to None
month = None
if month_entered.isdecimal() or month_entered.isdigit():
    month = int(month_entered)

# Step3: Checking Valid months for wind chill calculation
if month is not None and month in [11,12,1,2]:
    # Step4: Prompt user for temperature and wind spee
    temperature_entered = input("Enter the temperature between -50 and 50 °F: ")
    wind_speed_entered = input("Enter the wind speed between 3 and 120 mph: ")

    # Step5: Checking validity of temperature and wind speed entered.
    # Check the entry is correct
    temperature = None
    if temperature_entered.isdecimal() or temperature_entered.isdigit():
        temperature = float(temperature_entered)
    
    wind_speed = None
    if wind_speed_entered.isdecimal() or wind_speed_entered.isdigit():
        wind_speed = float(wind_speed_entered)

    # check if the temperature and wind speed are valid

    if temperature is None:
        print(f"Invalid input {temperature_entered}. Enter valid Temperature ")
    elif wind_speed is None:
        print(f"Invalid  input {wind_speed_entered}. Entered valid Wind Speed.")
    
    elif abs(temperature)>50 or wind_speed <3 or wind_speed>120:
        print(f"Invalid input. Temperature {temperature} must be between -50",
              f"and 50° F , and wind speed {wind_speed} between 3 and 120 mph.")
    
    else:
        wind_chill = (35.74 + 0.6215 * temperature-35.75 * (wind_speed**0.16)+0.4275* temperature * (wind_speed**0.16))
        print(f"Wind Chill: {wind_chill: .2f} °F for Month {month} with",
              f"Temperature {temperature} and wind speed {wind_speed}")

else:
    print(f"Wind Chill computation is not applicable for month {month_entered}.")