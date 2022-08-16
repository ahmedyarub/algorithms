class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s = ' ' + s
        pcnt, scnt, result = Counter(p), Counter(s[:len(p)]), []

        for i in range(1, len(s) - len(p) + 1):
            scnt[s[i - 1]] -= 1
            scnt[s[i + len(p) - 1]] += 1
            if pcnt == scnt:
                result.append(i - 1)

        return result
