def solution(matrix):
    matrix_sum = 0
    occupied_cols = set(())

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                occupied_cols.add(j)
            else:
                if j not in occupied_cols:
                    matrix_sum += matrix[i][j]

    return matrix_sum
