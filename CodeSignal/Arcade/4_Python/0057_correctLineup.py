def solution(athletes):
    return [athletes[i ^ 1] for i in range(len(athletes))]
