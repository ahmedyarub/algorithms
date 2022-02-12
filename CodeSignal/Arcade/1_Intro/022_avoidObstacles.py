def solution(inputArray):
    inputArray.sort()

    max_value = max(inputArray)

    for i in range(1, max_value - 1):
        invalid = False
        for j in range(i, max_value + 1, i):
            if j in inputArray:
                invalid = True
                break
        if not invalid:
            return i

    return max_value + 1
