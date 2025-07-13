# Good 
# 1: Proper comments to the function
# 2: No overuse of global variables
# 3: Defining proper function parameter data types

def add(x:int,y:int):
    """
    Returns the sum of two numbers
        `"""
    return x+y

# Good 
# 1:Descriptive global variable names
# 2:Type conversion from str to int
# 3:Handling bad user input

#Bad: Not handling the error occured
try:
    value1 = int(input("Enter the first number "))
    value2 = int(input("Enter the second number "))
    print(f"The sum of {value1} and {value2} is {add(value1,value2)}")

except ValueError as e:
    print(f"Oops {e}\n That was not vaild input try again")

except:
    print("Try again and enter the proper value")
