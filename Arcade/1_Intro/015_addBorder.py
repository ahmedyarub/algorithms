def solution(picture):
    result = ['*' * (len(picture[0]) + 2)]

    for i in range(len(picture)):
        result.append('*' + picture[i] + '*')

    result.append('*' * (len(picture[0]) + 2))
    return result
