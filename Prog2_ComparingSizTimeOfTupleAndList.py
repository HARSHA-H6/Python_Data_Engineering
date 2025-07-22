import sys
import timeit

# Define a tuple and list of 10 integers
tuple_data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Compare size using sys.getsizeof()
tuple_size = sys.getsizeof(tuple_data)
list_size = sys.getsizeof(list_data)

print(f"Size of tuple: {tuple_size} bytes")
print(f"Size of list: {list_size} bytes")

# Compare creation time using timeit.timeit()
tuple_time = timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9,10)", number=10000000)
list_time = timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9,10]", number=10000000)

print(f"Creation time for tuple (in seconds): {tuple_time}")
print(f"Creation time for list (in seconds): {list_time}")
