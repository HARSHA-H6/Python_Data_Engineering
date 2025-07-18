
details = {"Name":"Harsha", "City":"Bengaluru", "Pincode":561203}


friend_details = {1:"School",
                  2:"College",
                  3:"Neighbourhood"}


print(details.items())
choice = int( input("Enter the friend type: "))

if choice in friend_details:
    details["Friend_type"] = friend_details[choice]
    print(details.items())