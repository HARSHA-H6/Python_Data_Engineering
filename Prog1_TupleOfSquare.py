# Create a list of squares using 
square_list = []
for i in range(10):
    square_list.append(i**2)
# print(square_list)

# Create a tuple of square 
square_tuple = tuple(square_list)

print(f"The tuple of square of the numbers are : {square_tuple}")

print(f"The 3rd element : {square_tuple[2]}")
print(f"The 5rd element : {square_tuple[4]}")
print(f"The 7rd element : {square_tuple[6]}")

print(f"The first 3 elements: {square_tuple[:3]}")