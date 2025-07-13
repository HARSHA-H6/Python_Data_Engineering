import my_calculator

# Get input from user
try:
    num1= float(input("Enter the first Number:"))
    num2 = float(input("Enter the second Number: "))

except ValueError:
    print(f"Invalid input. Please enter numbers only")

sum_result = my_calculator.add(num1,num2)
difference_result = my_calculator.subtract(num1,num2)
multiply_result = my_calculator.multiply(num1,num2)
divide_result = my_calculator.divide(num1,num2)

print(f"Sum: {sum_result}")
print(f"Differnce: {difference_result}")
print(f"Product: {multiply_result}")
print(f"Division: {divide_result}")