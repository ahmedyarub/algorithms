def solution(lastNumberOfDays):
    if lastNumberOfDays in [28, 30]:
        return [31]
    else:
        return [28, 30, 31]
