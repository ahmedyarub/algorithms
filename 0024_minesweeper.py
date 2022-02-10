def solution(matrix):
    result = []

    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            count = 0
            for m in range(0 if i == 0 else i - 1, len(matrix) if i == len(matrix) - 1 else i + 2):
                for n in range(0 if j == 0 else j - 1, len(matrix[0]) if j == len(matrix[0]) - 1 else j + 2):
                    if not (i == m and j == n) and matrix[m][n]:
                        count += 1
            row.append(count)

        result.append(row)

    return result
