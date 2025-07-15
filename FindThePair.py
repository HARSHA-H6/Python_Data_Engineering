# Step1 :Take the input from the user
array = list(map(int,input("Enter the elements : ").split()))

# Step2 :Get the target from the user
target  = int(input("Enter the target"))

# create a empty list to store the pairs
solution =[]
for i in array:
    # Check wether the pair exists in the list
    if array.__contains__(target-i):
        # add the pair to the empty list
        solution.append(i)

# print the soulution
print(solution)