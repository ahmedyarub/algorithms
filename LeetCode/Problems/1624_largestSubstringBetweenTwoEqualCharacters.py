class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        result = -1
        first_pos = dict()

        for i, c in enumerate(s):
            if c not in first_pos:
                first_pos[c] = i
            else:
                result = max(result, i - first_pos[c] - 1)

        return result
