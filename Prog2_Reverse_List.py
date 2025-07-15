# Define the function the to reverse the function using the slicing 
def reverse_list(input_list):
    reversed_list = input_list[::-1]
    input_list.reverse()
    # Check the inbuilt and the custom reverse are giving the same result
    return reversed_list == input_list


input_list = list(map(int,input("Enter the elements in the list one by one by giving the space in between: ").split()))
# calling the reverse function
if reverse_list(input_list):
    print(f"The custom reverse method using slicing and the inbuilt reverse method gives the same result")
else:
    print(f"The custom reverse method using slicing and the inbuilt reverse method gives the different result")
