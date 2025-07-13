def greet_friend(name:str):
    """ Greets a friend by their name"""
    if name.isalpha():
        print(f" Hello {name}!, How are you today?")
    else:
        print(f"Enter the valid name which contains only the alphabetic characters")

name = input("Enter your name: ")
greet_friend(name)