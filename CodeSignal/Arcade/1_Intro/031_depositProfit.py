def solution(deposit, rate, threshold):
    return math.ceil(math.log(threshold / deposit, 1 + rate / 100))
