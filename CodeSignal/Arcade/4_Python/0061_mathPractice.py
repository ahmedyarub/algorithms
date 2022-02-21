def solution(numbers):
    return functools.reduce(lambda result, pair: result * pair[1] if pair[0] % 2 == 0 else result + pair[1],
                            enumerate(numbers), 1)
