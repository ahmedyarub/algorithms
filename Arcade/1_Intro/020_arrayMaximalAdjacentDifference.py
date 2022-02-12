def solution(inputArray):
    max_diff = abs(inputArray[1] - inputArray[0])

    for i in range(1, len(inputArray) - 1):
        cur_dif = abs(inputArray[i + 1] - inputArray[i])
        if cur_dif > max_diff:
            max_diff = cur_dif

    return max_diff
