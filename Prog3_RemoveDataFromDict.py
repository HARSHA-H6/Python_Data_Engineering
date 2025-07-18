
# Crete the dictionary
details ={"Name":"Harsha","City":"Bengaluru", "Pincode":561203}
#
# print the value by using the key
print(details["Name"])

revised_dict = details.copy()

print(revised_dict)
if "Pincode" in revised_dict:
    del revised_dict["Pincode"] # we must check if the key is present before del other wise it may throw error

value = revised_dict.pop("Name", None) #same here if the key is not present instead of throwing error it shows None
# pop() returns the value
print(value)
print(revised_dict)
