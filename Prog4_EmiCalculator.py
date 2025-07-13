
# Step1: Take user input for Principle 
principle_entered = input("Enter the Principle Amount: ")
roi_entered = input("Enter the rate of intrest: ")
years_entered = input("Enter the Time in years: ")

# Step2: Validate the input and convert into integer
principal = principle_entered.isdigit() and int(principle_entered) or None
roi = roi_entered.isdigit() and float(roi_entered) or None
years = years_entered.isdigit() and int(years_entered) or None

#Step3: Check if the user input is valid
if (principal is not None and roi is not None and years is not None and principal >0 and roi>0 and years>0):
    
    intrest_per_month = round(1*roi/{12*100},2)
    months = years*12

    emi = round(principal* intrest_per_month*(1+intrest_per_month)**months/((1+intrest_per_month)**months-1),2)
    balance = principal

    print(f"{'-'*65}")
    print(f"| {'Month ':^8} | {'EMI ':^8} | {'Intrest ':^10}",
          f"| {'Principle':^10} | {'Balance':^10} |")
    
    total_month = total_emi = total_intrest = total_principal = 0.0

    for month in range(1,months+1):
        intrest= round(balance*roi/(12*100),2)
        principal = round(emi-intrest,2)
        balance = round(balance-principal,2)

    if balance<0:
        principal = round(principal+balance,2)
        emi = round(principal+intrest,2)
        balance = 0

    total_month +=1; total_emi+=emi; total_intrest+= intrest; total_principal +=total_principal
    print(f"| {month:^8} | {emi:^10} | {intrest: ^10} | {principal:^10}"\
          f"| {balance:^10}")
    
    print(f"{'-'*65}")
    print(f"| {'Total':^8} | {total_emi:^10.2f} | {total_intrest:^10.2f}",
      f"| {total_principal:^10.2f} | {balance:^10 .2f} | ")
    print(f"{'-'*65}")

else:
    print(f"Invalid Input: {principle_entered},{roi_entered},{years_entered}"\
          "are not valid numbers")