def solution(sequence):
    return max(sequence) - min(sequence) - len(sequence) + 1
