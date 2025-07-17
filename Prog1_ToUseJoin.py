
# create the empty list to store the places
places = []

for i in range(1,6):
# Take the input from the user
    place = input(f"Enter the name of the place {i}: ")
    places.append(place)

print(f"The places present in the list: {places}")

# Initalizing the empty string to store the answer
revised_places=""

for index, place in enumerate(places):
    revised_places += place.upper()

    if index != len(places)-1:
        revised_places+="," 


print(f"The places present in the list: {revised_places}")
