#Bad

def calculate_area(radius):
    return 3.14*radius**2

#GOOD
#Specifying a Global Constant for PI

PI = 22/7

def calculate_area(radius:int):
    return PI*radius**2

radius = 2
print(f"Area of a Circle with radius = {radius} is {calculate_area(radius)}")
