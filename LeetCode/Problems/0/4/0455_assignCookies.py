class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        gi = si = 0

        result = 0
        while gi < len(g) and si < len(s):
            if g[gi] <= s[si]:
                result += 1
                gi += 1

            si += 1

        return result
