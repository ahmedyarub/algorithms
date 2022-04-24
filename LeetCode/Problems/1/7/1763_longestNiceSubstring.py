class Solution:
    def longestNiceSubstring(self, s):
        chars = set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in chars:
                return max(map(self.longestNiceSubstring, [s[:i], s[i + 1:]]), key=len)
        return s
