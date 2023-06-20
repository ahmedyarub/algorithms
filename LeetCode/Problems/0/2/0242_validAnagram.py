class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc = Counter(s)

        for ct in t:
            if ct not in sc:
                return False

            sc[ct] -= 1

        return not any(sc.values())
