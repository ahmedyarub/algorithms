def solution(a):
    result = 0

    while a:
        result = (result << 1) + a % 2
        a //= 2

    return result
