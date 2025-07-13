#  BAD 
# Cryptic variable names
x=10
y = 20
z = x+y
print(f"The sum of {x} and {y} is {z}")
def add(x:int,y:int):
    """
    This is descriptive comments
    """
    return x+y

total_sum=100
bonus_points=200
final_score = add(total_sum,bonus_points)

print(final_score)
print(f"{type(final_score)}")
