import re
# Take the input from the user
email = input("Enter the mail address: ")

pattern = r'^[a-zA-Z0-9.%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'

if re.match(pattern,email):
    print(f"{email} is a valid email")

else: 
    print(f"{email} is not a valid email")