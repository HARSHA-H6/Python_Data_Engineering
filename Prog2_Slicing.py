
input_string = input("Enter the string : ")

first_character = input_string[0]
middle_character = input_string[len(input_string)//2]
last_character = input_string[-1]

new_string = first_character+middle_character+last_character

print(new_string)