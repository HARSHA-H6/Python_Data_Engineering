# Define the constant for PI
PI = 22/7

# Take input for radius of the circle in inches
radius_inch = float(input("Enter the radius of circle in inches: "))
# Convert inches to cm using 1 in = 2.54 cm
radius_cm =radius_inch*2.54

# Compute circumference and area in centimeters and square centimeters
circumference_cm = 2*PI*radius_cm
area_cm_square = PI*(radius_cm**2)

# Print the results
#    : .2f helps to round of the value to the 2 places after the decimal
print(f"Circumference of the circle is {circumference_cm: .2f} cm and",
      f"Area of the  Circle is {area_cm_square: .2f} sqcm")