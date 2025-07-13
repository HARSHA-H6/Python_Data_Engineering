# Use the in-bulit help function to know more about other function
# help(print)

# Step1: Take User inputs for name, places and year
user_name = input("Enter the user name ")
first_place = input("Enter the first place you would like to vist ")
second_place = input("Enter the second place you would like to vist ")
third_place = input("Enter the third place you would like to vist ")
year = input("Enter the year you visit ")

# Step2: Print the user and the places to visit for the year
# use sep=',' for seperation and end='' for continuing in the same line
print(f"\nHello {user_name} and places to vist are {first_place}",second_place,third_place,sep=',',end=' ')
print(f'in the year {year}')