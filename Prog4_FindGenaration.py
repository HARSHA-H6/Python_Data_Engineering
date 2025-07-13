# Step1: Enter the birth year
birth_year=int(input("Enter birth year : "))

# Step2: Print the Generation using python shorthand condition 
print(f'Birth yera is {birth_year}',
      f'Is Baby Boomer: {birth_year>=1946 and birth_year<=1964}',
      f'Is GenX: {birth_year>=1965 and birth_year<=1980}',
      f'Is Millennial: {birth_year>=1981 and birth_year<=1996}',
      f'Is Gen Z: {birth_year>=1997 and birth_year<=2012}',
      f'Is Gen Alpha: {birth_year>=2013 and birth_year<=2025}' , sep='\n')