def solution(sequence):
    for i in range(1, len(sequence)):
        if sequence[i] <= sequence[i - 1]:
            return increasing([x for j, x in enumerate(sequence) if j != i]) or increasing(
                [x for j, x in enumerate(sequence) if j != i - 1])

    return True


def increasing(sequence):
    for i in range(1, len(sequence)):
        if sequence[i] <= sequence[i - 1]:
            return False

    return True
