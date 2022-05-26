class Solution:
    def freqAlphabets(self, s: str) -> str:
        mp = {str(i) + ('#' if i > 9 else ''): chr(ord('a') + i - 1) for i in range(1, 27)}
        result, i, l = [], 0, len(s)

        while i < l:
            if i + 2 < l and s[i:i + 3] in mp:
                result.append(mp[s[i:i + 3]])
                i += 3
            else:
                result.append(mp[s[i:i + 1]])
                i += 1

        return "".join(result)
