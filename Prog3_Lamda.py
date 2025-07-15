# Take the input from the user
input_list = list(map(int,input("Enter the numbers one by one giving space inbetween them: ").split()))

# create the another list which stores the doubled value of original list
doubled_list = list(map(lambda x:x*2,input_list))

# Print the Result
print(f"Original List : {input_list}")
print(f"Doubled List : {doubled_list}")