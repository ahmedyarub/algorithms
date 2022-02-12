def solution(s1, s2):
    chars1 = dict()
    common_chars = 0

    for i in range(len(s1)):
        chars1[s1[i]] = chars1.get(s1[i], 0) + 1

    for i in range(len(s2)):
        char_count = chars1.get(s2[i], 0)
        if char_count > 0:
            common_chars += 1
            chars1[s2[i]] = char_count - 1

    return common_chars
