def solution(a):
    result = 0

    for n in reversed(a):
        result = (result << 8) + n

    return result
