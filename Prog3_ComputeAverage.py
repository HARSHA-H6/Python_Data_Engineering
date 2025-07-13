
def compute_avg(data):
    """sum_data = sum(data)
    len_data = len(data)
    return round(sum_data/len_data,3)"""
    return round(sum(num_list)/len(num_list),2)

num_list = [10,20,30,40,50]
print(f"The average of the give list {num_list} is {compute_avg(num_list):.2f}")