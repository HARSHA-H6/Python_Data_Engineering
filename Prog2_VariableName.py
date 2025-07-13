# BAD
# Naming the variable casually without any meaning
x = 100
y = 200
z = x+y
print(f"The value z is {z}")


# GOOD
# Descriptive global variable names having meaningful name

total_sum = 10
bonus_points = 20
final_score = total_sum+bonus_points

print(f"Final Score is {final_score}")