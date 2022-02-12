def solution(inputArray):
    max_length = 0
    strings = []

    for i in range(len(inputArray)):
        cur_length = len(inputArray[i])
        if cur_length > max_length:
            max_length = cur_length
            strings = [inputArray[i]]
        elif cur_length == max_length:
            strings.append(inputArray[i])

    return strings
