class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        bad = [i for i in range(len(s1)) if s1[i] != s2[i]]

        return not len(bad) or (len(bad) == 2 and s1[bad[0]] == s2[bad[1]] and s1[bad[1]] == s2[bad[0]])
