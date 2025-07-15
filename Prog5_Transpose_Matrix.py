# Function to transpose the matrix
def transpose_matrix(matrix):
    ROWS, COLS = len(matrix),len(matrix[0])
    transposed_matrix = [[0,0,0],[0,0,0],[0,0,0]]

    for row in range(ROWS):
        for col in range(COLS):
            transposed_matrix[col][row] = matrix[row][col]

    return transposed_matrix
# Intialize the 2D array
matrix = [[1,2,3],[4,5,6],[7,8,9]]

# Calling the function
transposed_matrix = transpose_matrix(matrix)

# Print the original Matrix
print("Original Matrix: ")
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(matrix[row][col], end=' ')
    print()

# Print the transposed matrix
print("Transposed Matrix: ")
for row in range(len(transposed_matrix)):
    for col in range(len(transposed_matrix[row])):
        print(transposed_matrix[row][col], end=' ')
    print()