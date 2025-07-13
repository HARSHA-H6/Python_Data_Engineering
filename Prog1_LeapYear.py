# Step1: Prompt user to enter a year and assign to global variable year_input
year_input = input("Enter a year: ")

# Step2: Check if input is a digit
if year_input.isdigit():
    # Step3: Convert input to integer and assign it to the local variable name
    year = int(year_input)

    # Step4: Check if the year is at least 1582 which is the start of 
    # the Gregorian calendar
    if year >= 1582:
        # Step5: Divided by 100 means century year (ending with 00)
        # and century year divided by 400 is leap year
        if (year%100 == 0) and (year%400 == 0):
            print(f"The year {year} is a leap year")

        # Step6: Check if the year is divisible by 4 and not by 100
        elif (year % 4==0) and (year %100 !=0):
            print(f"The year {year} is a leap year")
        else:
            print(f"The year {year} is not a leap year")
    
    else:
        print(f"The entered year {year} must be 1582 or later.")

else:
    print(f"Invalid year {year_input} entered. Please enter a valid year.")