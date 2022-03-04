def solution(commands):
    count = 0
    same = True
    for c in commands:
        if c == 'A':
            if same:
                count += 1
        elif same:
            same = False
        else:
            same = True
            count += 1

    return count