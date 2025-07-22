# Function to swap using tuple
def swap(x, y):
    return y, x  # Returns two values as a tuple

# Take the input from the user 
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("\nInitial Value of a & b are")
print(f"a = {a}")
print(f"b = {b}")

# Swapping using function
x, y = swap(a, b)

print("\nAfter swapping (using function):")
print(f"x = {x}")
print(f"y = {y}")
