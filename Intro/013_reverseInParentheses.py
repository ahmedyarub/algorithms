def solution(inputString):
    output = ''
    i = 0

    while i < len(inputString):
        cur_char = inputString[i]
        if cur_char == '(':
            closing_index = findClosingParantheses(inputString, i + 1)
            output += solution((inputString[i + 1:closing_index]))[::-1]
            i = closing_index + 1
        else:
            output += inputString[i]
            i += 1

    return output


def findClosingParantheses(inputString, start):
    open_paran = 0
    for i in range(start, len(inputString)):
        if inputString[i] == ')':
            if open_paran == 0:
                return i
            else:
                open_paran -= 1
        elif inputString[i] == '(':
            open_paran += 1
