
def find_max_min(num_list):
    """if the list is empty it returns false 
    if the list is not empty it returns true"""
    if not num_list:
        print(f"Oops! I think the list is empty")
        return None
    
    min_val = min(num_list)
    max_val = max(num_list)
    return min_val,max_val

num_list = [10,5,20,15,30]
minimun_number,maximum_number = find_max_min(num_list)
print(f"Original List : {num_list}",
      f"Minimum Number in the list is: {minimun_number}",
      f"Maximum Number in the list is: {maximum_number}", sep='\n')