class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, cur = 0, 1
        result = 0

        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                result += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1

        return result + min(prev, cur)
