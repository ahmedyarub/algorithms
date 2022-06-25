class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2) or (Counter(s3) - Counter(s1 + s2)):
            return False

        @lru_cache(maxsize=None)
        def traverse(i1: int, i2: int, i3: int) -> bool:
            nonlocal s1, s2, s3

            while i3 < len(s3):
                if i1 < len(s1) and s3[i3] == s1[i1] and i2 < len(s2) and s3[i3] == s1[i1]:
                    return traverse(i1 + 1, i2, i3 + 1) or traverse(i1, i2 + 1, i3 + 1)
                elif i1 < len(s1) and s3[i3] == s1[i1]:
                    i1 += 1
                elif i2 < len(s2) and s3[i3] == s2[i2]:
                    i2 += 1
                else:
                    return False

                i3 += 1

            return True

        return traverse(0, 0, 0)
