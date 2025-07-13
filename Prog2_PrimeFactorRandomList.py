import random

# Function to create random List
def create_random_list():
    # Step 1: Take the input from the user
    lower_limit = input("Enter the lower limit>1: ")
    upper_limit = input("Enter the upper limit: ")
    size_entered = input("Enter the total random number to generate: ")

    # Step 2: Validate the given input
    lower = (lower_limit.isdigit() and int(lower_limit) or None)
    upper =(upper_limit.isdigit() and int(upper_limit) or None)
    size = (size_entered.isdigit() and int(size_entered) or None)
    
    # Step3: Initialize random list 
    random_list=[]
    if (lower is not None and upper is not None and size is not None and
        lower > 0 and upper > lower and size>1 and size< upper-lower):
        random_list = [random.randint(lower,upper) for i in range(size)]
    else:
        print(f"Invalid Entry Lower limit {lower_limit}, or",
              f"Upper Limit {upper_limit} or range {size_entered}.")
    
    return random_list

print(create_random_list())