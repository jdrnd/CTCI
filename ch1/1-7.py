def rotate_90_right(matrix):
    size = len(matrix)
    print(size)
    new_matrix = [[0 for x in range(size)] for y in range(size)]

    for i in range(0, size):
        row = matrix[i]
        for j in range(0, size):
            new_matrix[j][size - 1 - i] = matrix[i][j]

    return new_matrix

def rotate_90_right_inplace(matrix):
    size = len(matrix)



test_matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(rotate_90_right(test_matrix))
