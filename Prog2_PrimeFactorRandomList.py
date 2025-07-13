import random
# Function to get prime factors for the random list and return
# Dict fo random numbers to prime factors
def get_random_prime_factors(random_list):
    get_random_prime_factor_dict = {}
    for random_number in random_list:
        get_random_prime_factors = get_prime_factors(random_number)
        get_random_prime_factor_dict[random_number]= get_random_prime_factors
    return get_random_prime_factor_dict

# Function to get the prime factors of a number
def get_prime_factors(number):
    prime_factors=[]
    if type(number) is not int or number<2:
        return prime_factors
    while number %2 ==0:
        prime_factors.append(2)
        number = number//2
    if number==1:
        return prime_factors
    
    start_range = 3
    stop_range = number**0.5<3 or number**0.5
    skip_range = 2
    # Setting the start, stop and skip value of the range
    for prime_number in range(start_range, int(stop_range)+1,skip_range):
        while number %prime_number==0:
            prime_factors.append(prime_number)
            number = number//prime_number
    if number>2:
        prime_factors.append(number)
    # Return the prime factors
    return prime_factors

# Function to get a dict of prime numbers that are factors to list of random numners
def get_prime_factor_random_list(random_prime_factor_dict):
    prime_random_dict={}
    
    for random_number in random_prime_factor_dict:
        random_prime_factors = random_prime_factor_dict[random_number]

        unique_prime_factors = set(random_prime_factors)

        for prime_factor in unique_prime_factors:
            prime_random_list = prime_random_dict.get(prime_factor)
            if prime_random_list is None:
                prime_random_list = list()
                prime_random_dict[prime_factor]= prime_random_list
            prime_random_list.append(random_number)
        return prime_random_dict
    
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

random_list = create_random_list()
print(f"Random list generated is {random_list}")

if(len(random_list)>0):
    random_prime_factor_dict = get_random_prime_factors(random_list)

    prime_random_dict = get_prime_factor_random_list(random_prime_factor_dict)

    print(f"Random Nnumber and its prime factors {random_prime_factor_dict}")
    print(f"Prime Factor to Random List {prime_random_dict}")

else:
    print(f"Random List {random_list} is Empty. Enter proper Limits")