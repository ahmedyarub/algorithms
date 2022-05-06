class Solution:
    def checkString(self, s: str) -> bool:
        i = 0

        while i != len(s) and s[i] == 'a':
            i += 1

        return 'a' not in s[i:]