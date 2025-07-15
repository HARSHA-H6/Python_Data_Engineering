# Step1: assign the value to the list

colors = ["Red", "Green", "Pink", "Blue", "Black", "Purple", "Yellow", "Magenta", "Brown"]

revised_list = []
i=0

for color in colors:
    # Checking if the index is 0 or 2 or 5
    if i not in[0,2 ,5]:
        revised_list.append(color)
    i+=1

# PRint the result
print(f"The Original List is : {colors}")
print(f"The revised List is : {revised_list}")