
# Take the input from the user

input_string = input("Enter the input string: ")

digits=0
letters=0
special_letter = 0

for i in input_string:
    if i.isdigit():
        digits+=1
    elif i.isalpha():
        letters+=1
    else:
        special_letter+=1

print(f"The number of Digits present in the String is: {digits}",
      f"The number of letters present in the string is: {letters}",
      f"The number of special characters in the string is : {special_letter}", sep='\n')

