from collections import Counter


def solution(encryptedText):
    return Counter(encryptedText).most_common(1)[0][0]
