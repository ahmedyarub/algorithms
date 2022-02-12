def solution(image):
    result = []

    for i in range(1, len(image) - 1):
        row = []
        for j in range(1, len(image[0]) - 1):
            row.append(
                (
                        image[i - 1][j - 1] + image[i][j - 1] + image[i + 1][j - 1] +
                        image[i - 1][j] + image[i][j] + image[i + 1][j] +
                        image[i - 1][j + 1] + image[i][j + 1] + image[i + 1][j + 1]
                ) // 9
            )

        result.append(row)

    return result
