def solution(trainingData):
    correct = list(filter(lambda pair: pair[1] == 1, trainingData))

    if len(correct) == 0:
        return 0

    s = 0
    for i in correct:
        s += i[0]

    return s / len(correct)
