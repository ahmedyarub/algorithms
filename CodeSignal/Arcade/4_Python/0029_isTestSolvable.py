def solution(ids, k):
    digitSum = lambda id: sum(int(digit) for digit in str(id))

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
