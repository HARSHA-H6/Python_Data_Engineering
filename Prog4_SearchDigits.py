# Import the regex package
import re

# take the input from the user
input_text = input("Enter the input text: ")

# find all the digits present in the string
digits = re.findall(r"\d", input_text)
# print all the digits
print(digits)  
