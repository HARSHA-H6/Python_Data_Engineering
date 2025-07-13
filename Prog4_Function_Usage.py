# BAD
# 1:No proper comments for the function
# 2:Bad use of Global Variable

def calc(y):
    return total_sum +y

# GOOD
# 1:Proper comments to the function
# 2:No overuse of Global Variables

def calculate_sum(x:int,y:int):
    """
    Returns the sum of two numbers
    """
    return x+y

total_sum =10
bonus_points = 20
print(f"Data Types of total_sum is {type(total_sum)} and "
      f"bonus_points is {type(bonus_points)}")

final_score = calculate_sum(total_sum,bonus_points)

print(f'Final Score is {final_score}')