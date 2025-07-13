import random
# Function to generate the random numbers
def generate_random_numbers(lower_value:int,upper_value:int,random_value:int):
    random_list=[]
    for i in range(random_value):
        random_list.append(random.randint(lower_value,upper_value))
    return random_list
# Function to generate the Fibonacci list
def generate_fibonacci(upper_limit:int):
    fibbnoicci_list=[0,1]
    while True:
          next_fib = fibonacci_list[-1]+fibonacci_list[-2]
          if next_fib>upper_limit:
               break
          fibonacci_list.append(next_fib)
    return fibonacci_list

# Function to get the numbers which are comman in both the list
def get_comman(fibonacci_list,random_list):
    return list(set(fibonacci_list) & set(random_list))

# Take the user input from the user
try:
    lower_value = int(input("Enter the lower limit that is >1: "))
    upper_value = int(input("Enter the upper value that is <100: "))
    random_value = int(input("Enter the random value: "))
    # Validate the user input
    if lower_value>upper_value or random_value<1:
            print(f"Please enter the valid input")
            quit()
except ValueError as ex:
    print(f"Please Enter the proper input ","The current input has the following error{ex}")
    quit()

random_list = generate_random_numbers(lower_value,upper_value,random_value)
print(f"Random List: {random_list}")
upper_limit=max(random_list)

fibonacci_list=generate_fibonacci(upper_limit)
print(f"Fibbnoicci List: {fibonacci_list}")

comman_list = get_comman(fibonacci_list,random_list)
# print the final output
print(f"The common element in both the list is {comman_list}")

