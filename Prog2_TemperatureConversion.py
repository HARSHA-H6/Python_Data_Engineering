# Step1: Take input from the user
temperature_entered = input("Enter the temperature: ")

# Step2: Check if Temperature is in digit, then take up conversion

if temperature_entered.isdigit():
    temperature = float(temperature_entered)
    # Step3: take input for unit and check to perform coversion accordingly
    unit = input("Enter the unit of temperature (C for Celsius, F for Fahrenheit): ")
    match unit:
        case 'C'|'c':
            celcius = temperature
            fahrenheit = (celcius*9/5)+32
            print(f"{celcius} °C is equal to {fahrenheit:.1f}°F")

        case 'F'|'f':
            fahrenheit = temperature
            celcius = (fahrenheit-32)*5/9
            print(f"{fahrenheit} °F is equal to {celcius: .1f}°C")

        case _:
            print(f"Invalid Unit {unit}. Please enter 'C' for Celsius or 'F' for Fahrenheit. ")
else:
    print(f"Invalid Temperature {temperature_entered}. Please enter digits")