def solution(participants):
    return [i for i, x in enumerate(participants) if x < i]
