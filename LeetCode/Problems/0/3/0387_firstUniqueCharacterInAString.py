class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)

        for i, c in enumerate(s):
            if counts[c] == 1:
                return i

        return -1
