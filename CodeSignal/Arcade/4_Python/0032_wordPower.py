def solution(word):
    num = {w: ord(w) - ord('a') + 1 for w in word}
    return sum([num[ch] for ch in word])
