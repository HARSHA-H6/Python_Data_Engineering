# Input: Get the harmonic value N from user
N = int(input("Enter a harmonic value N (N must be > 0): "))

# Check if N is not zero or negative
if N <= 0:
    print("Harmonic value N must be greater than 0.")
else:
    harmonic = 0.0
    for i in range(1, N + 1):
        harmonic += 1 / i

    # Output: Print the Nth harmonic number
    print(f"The {N}th Harmonic number is: {harmonic:.4f}")
