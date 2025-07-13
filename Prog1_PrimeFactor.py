
# Function to get the prime factors of a number
def get_prime_factors(number):
    # Step1: Initialize an empty list to store the prime factors
    prime_factors=[]
    # Step2: Early return if validataion failed which is to validate the input 
    # number is integer and greater than 2
    if type(number) is not int or number<2:
        return prime_factors
    # Step3: Get Prime factors of 2
    while number %2 ==0:
        prime_factors.append(2)
        number = number//2

    if number==1:
        return prime_factors
    
    start_range = 3
    stop_range = number**0.5<3 or number**0.5
    skip_range = 2
    # Step 5: Setting the start, stop and skip value of the range
    for prime_number in range(start_range, int(stop_range)+1,skip_range):
        while number %prime_number==0:
            prime_factors.append(prime_number)
            number = number//prime_number

    
    if number>2:
        prime_factors.append(number)
    # Return the prime factors
    return prime_factors

# Taking the user input from the user
number = int(input("Enter the number: "))
print(f"Prime factors of the number {number} is {get_prime_factors(number)}")



