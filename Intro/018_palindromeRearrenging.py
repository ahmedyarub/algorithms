def solution(inputString):
    char_frequency = dict()

    for i in inputString:
        if i in char_frequency:
            char_frequency[i] += 1
        else:
            char_frequency[i] = 1

    has_odd = False
    for key, value in char_frequency.items():
        if value % 2 == 1:
            if has_odd:
                return False
            else:
                has_odd = True

    return (not has_odd) or (len(inputString) % 2 == 1 and has_odd)
