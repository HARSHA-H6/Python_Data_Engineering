import random

# Function to flip the coin
def flip_coin(times:int):
    tails=0
    heads = 0
    # Assigning the values to head or tail
    for _ in range(times):
        coin_toss = random.random()
        if(coin_toss<0.5):
            tails+=1
        else:
            heads+=1
    
    # Printing the final result
    print(f"The percentage of the heads is {(heads/times)*100:.2f}%",
          f"The percentage of the tails is {(tails/times)*100:.2f}%")
    # end of the function

# Take input from the user
times_entered  = input("How many times does the coin should be flipped: ")
# Validate the user input
if times_entered.isdigit():
    times = int(times_entered)
    # Check the input is positive number
    if times>1:
        flip_coin(times)
    else:
        print("Please enter the positive number greater than 0 ")
else: 
    print(f"Invalid input. Please enter the positive integer")

    