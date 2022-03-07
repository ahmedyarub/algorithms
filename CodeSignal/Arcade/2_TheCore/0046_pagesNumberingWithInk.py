def solution(current, numberOfDigits):
    while numberOfDigits >= 0:
        numberOfDigits -= len(str(current))
        current += 1
    return current - 2
