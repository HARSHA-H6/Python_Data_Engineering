# Define the function to get the factorial
def factorial(number:int):
    # Define the conditions
    if number<1:
        return 1
    # Calling the recursive call
    return factorial(number-1)*number

# Take the input from the user
number_entered = input("Enter the number whose factorial is needed: ")
number = number_entered.isdigit() and int(number_entered)  or None

# Print the final output
print(f"The factorial of the given number {number} is {factorial(number)}")