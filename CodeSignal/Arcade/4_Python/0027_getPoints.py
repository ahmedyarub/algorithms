def solution(answers, p):
    questionPoints = lambda index, answer: index + 1 if answer else -p

    res = 0
    for i, ans in enumerate(answers):
        res += questionPoints(i, ans)
    return res
