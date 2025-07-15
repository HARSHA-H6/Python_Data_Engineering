import sys
# Function to get the power of 2
def power_of_two(n: int):
    if 0 <= n < 31:
        print(f"Table of powers of 2 up to 2^{n}:")
        for i in range(n + 1):
            print(f"2^{i} = {2 ** i}")
    else:
        print("Please enter a value of N such that 0 <= N < 31.")

# Main logic to read from command-line
if len(sys.argv) != 2:
    print("")
else:
    arg = sys.argv[1]
    if arg.isdigit():
        n = int(arg)
        power_of_two(n)
    else:
        print("Please enter a valid integer value for N.")
