def solution(inputArray):
    max_product = inputArray[0] * inputArray[1]
    for i in range(1, len(inputArray) - 1):
        if max_product < inputArray[i] * inputArray[i + 1]:
            max_product = inputArray[i] * inputArray[i + 1]

    return max_product
