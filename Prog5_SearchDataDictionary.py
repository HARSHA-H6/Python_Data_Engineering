
# Create the dictionary to store the friends details

friends_details = {
    "Friend1":{"City": "Bengaluru",
               "Pincode":561203,
               "Email":"friend1@gmail.com",
               "PhoneNumber":123456789} ,

    "Friend2":{"City": "Chennai",
               "Pincode":961203,
               "Email":"friend2@gmail.com",
               "PhoneNumber":234567891} ,

    "Friend3":{"City": "Pune",
               "Pincode":161203,
               "Email":"friend3@gmail.com",
               "PhoneNumber":345678912} ,

    "Friend4":{"City": "Mysore",
               "Pincode":631203,
               "Email":"friend4@gmail.com",
               "PhoneNumber":456789123} 
}

# Take the input from the user 
friend_name = input("Enter the friend name: ")
detail = input("Enter the detail you need : ")

# find the data entered is present in the dictionary
if friend_name in friends_details:
    
    if detail in friends_details[friend_name]:

        print(f" {friend_name}'s {detail} is : {friends_details[friend_name][detail]}")
    
    else:
        print("Invalid detail type")

else:
    print("Friend not found ")
