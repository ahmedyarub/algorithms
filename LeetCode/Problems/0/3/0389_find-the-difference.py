class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ch = 0

        for c in s:
            ch ^= ord(c)

        for c in t:
            ch ^= ord(c)

        return chr(ch)
