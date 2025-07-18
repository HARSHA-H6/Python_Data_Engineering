# Merge the two dictionary

# Create first dictionary
friend_detials = {"Name":"Hari","City":"Andhra","Pincode":561204}

# Create another dictionary

additional_details = {"Email":"hari123456@gmail.com" , "Phone":987654321}

# Method 1: using copy and update
# merge using update
merged_update = friend_detials.copy()  #copy the first dictionary
# Transfert the additional dictionary by using the dictionary
merged_update.update(additional_details)

# Print the result
print(f"Merged Using the copy() and update() :{merged_update}")

# Method 2:Using unpacking 
merged_unpacking = {**friend_detials,**additional_details}
# Print result
print(f"Merged using unpacking ** :{merged_unpacking}")

# Method 3: Using | operator

merged_union = friend_detials | additional_details

print(f"Merged using the union | : {merged_union}")

# Method 4: Using the |=

merged_inplace = friend_detials.copy()
merged_inplace |= additional_details

print(f"Merged using the inplace copy() and |=  : {merged_inplace}")