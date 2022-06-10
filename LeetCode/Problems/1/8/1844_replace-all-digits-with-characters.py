class Solution:
    def replaceDigits(self, s: str) -> str:
        return "".join([chr(ord(s[i - 1]) + int(c)) if c.isnumeric() else c for i, c in enumerate(s)])
