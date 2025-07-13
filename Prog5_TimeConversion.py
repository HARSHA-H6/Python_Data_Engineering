# Step1: take input for time duration in total_seconds
total_seconds = int(input("Enter the total seconds: "))

# Step2: Convert seconds to hours, minutes and seconds using
# floor division and modulo opertor

hours = total_seconds//3600
minutes = (total_seconds%3600)//60
seconds = total_seconds%60

# Print the coverted time duration

print(f"Time duration of {total_seconds} seconds in the HH:MM:SS format is",
      f"{hours:02d}:{minutes:02d}:{seconds:2d}")