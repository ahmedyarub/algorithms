def solution(statues):
    return max(statues) - min(statues) - len(statues) + 1
