class Solution:
    def makeGood(self, s: str) -> str:
        result = s

        for i in range(len(s) - 1):
            if s[i].lower() == s[i + 1].lower() and s[i] != s[i + 1]:
                return self.makeGood(s[:i] + s[i + 2:])

        return result
