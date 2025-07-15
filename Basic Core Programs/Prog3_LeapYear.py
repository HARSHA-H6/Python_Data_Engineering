
# Function to check the year is leap or  not

def is_leap_year(year:int):

    if(year%400==0):
        print(f"The year {year} is a leap year.")
    elif(year%4==0 and year%100!=0):
        print(f"The year {year} is a leap year.")
    
    else:
        print(f"The year {year} is not a leap year.")

# Take the user input
year_entered = input("Enter the year: ")

# Validate the user entered input
if year_entered.isdigit():
    year = int(year_entered)
    # After the 1582 ,The Georgian calander starts
    if(year>=1582):
        is_leap_year(year)
    else:
        print("Enter the years which is 1582 or later.")
else:
    print("Please enter the valid year.")