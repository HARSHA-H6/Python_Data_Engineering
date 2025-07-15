# Step1: Take the input from the user
# Assign to the descriptive variable
user_name = input("Enter your name: ")

# Check the user_input has more than 3 characters
if(len(user_name)>3):
    # print the expected output
    print(f"Hello {user_name}, How are you ?")

else:
    print(f"Please enter the valid name whose length is more than 3")