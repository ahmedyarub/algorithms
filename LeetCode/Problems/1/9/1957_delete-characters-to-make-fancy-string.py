class Solution:
    def makeFancyString(self, s: str) -> str:
        result = [s[0]]

        for i in range(1, len(s) - 1):
            if s[i] != s[i - 1] or s[i] != s[i + 1]:
                result.append(s[i])

        return "".join(result + ([s[-1]] if len(s) > 1 else []))
