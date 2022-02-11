def solution(n):
    result = 9
    for i in range(1, n):
        result = (result * 10) + 9

    return result
