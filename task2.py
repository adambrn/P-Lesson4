def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    transposed_matrix = [[0 for _ in range(rows)] for _ in range(columns)]

    for i in range(rows):
        for j in range(columns):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transposed = transpose_matrix(matrix)
for row in transposed:
    print(row)

