def solution(morning, evening):
    return [min([i, j]) for i, j in zip(morning, evening)], [max([i, j]) for i, j in zip(morning, evening)]
