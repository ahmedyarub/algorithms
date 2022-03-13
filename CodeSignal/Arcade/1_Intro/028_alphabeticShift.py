def solution(inputString):
    return "".join(chr((ord(i) - ord('a') + 1) % 26 + ord('a')) for i in inputString)
