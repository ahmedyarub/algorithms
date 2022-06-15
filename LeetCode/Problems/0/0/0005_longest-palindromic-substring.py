class Solution:
    def longestPalindrome(self, s: str) -> str:
        result: str = ''
        for i in range(len(s)):
            for oe in [0, 1]:
                offset = 0
                while i - offset - oe >= 0 and i + offset + 1 < len(s) \
                        and s[i - offset - oe] == s[i + offset + 1]:
                    offset += 1
                offset -= 1
                result = max([result, s[i - offset - oe:i + offset + 2]], key=len, default='')

        return result
