def zero_row(matrix, rownum):
    size = len(matrix)
    for i in range(0, size):
        matrix[rownum][i] = 0

def zero_column(matrix, columnnum):
    size = len(matrix)
    for i in range(0, size):
        matrix[i][columnnum] = 0


def zero_cross_matrix(matrix):
    print(matrix)
    size = len(matrix)
    zeros = []
    for i in range(0, size):
        for j in range(0, size):
            if matrix[i][j] == 0:
                zeros.append([i, j])
    for pair in zeros:
        zero_row(matrix, pair[0])
        zero_column(matrix, pair[1])

    print(matrix)
    return matrix

test_matrix = [
    [0, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 0, 12],
    [13, 14, 15, 0]
]

zero_cross_matrix(test_matrix)
