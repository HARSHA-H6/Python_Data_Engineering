
# Function to caluculate the sum of the list
def sum_list(input_list):
    result =0
    for _ in input_list:
        result+=_
    return result
# Step1 : take the input from the user
input_list = list(map(int,input("Enter the all the elements given space in between: ").split()))

# check weather the inbulit sum and the custom sum gives same result
if sum(input_list)==(sum_list(input_list)):
    print(True)
else:
    print(False)