class Solution:
    def greatestLetter(self, s: str) -> str:
        mp, result = dict(), ""

        for c in s:
            mp[c] = True
            if (c.islower() and c.upper() in mp) or (c.isupper() and c.lower() in mp):
                result = max(result, c.upper())

        return result
