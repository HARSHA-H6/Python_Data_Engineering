import math

def calculate_car_loan_payment(principal:int, years:int,annual_roi):
    # Calculate the monthly intrest rate by using the annual interst rate
    monthly_intrest_rate = (annual_roi/100)/12

    # calculate the total number of monthly payments
    months = years*12

    if monthly_intrest_rate == 0.0:
        monthly_payment = principal/months
    
    else:
        emi = round(principal*monthly_intrest_rate*(1+monthly_intrest_rate)**months/((1+monthly_intrest_rate)**months-1),4)
    
    return emi
# Step 1: Take the user input

principal_entered = input("Enter the principal amount: ")
years_entered = input("Enter the years: ")
annual_intrest_entered = input("Enter the annual intrest rate: ")

# Step 2: validate the user entered value

principal = principal_entered.isdigit() and int(principal_entered) or None
years = years_entered.isdigit() and int(years_entered) or None
annual_roi = annual_intrest_entered.isdigit() and int(annual_intrest_entered) or None

if(principal is None and years is  None and annual_roi is  None ):
    print("Please, Enter the valid value")
    exit()

monthly_payment = calculate_car_loan_payment(principal,years,annual_roi)
print(f"Monthly car loan payment: {monthly_payment :.3f}")

