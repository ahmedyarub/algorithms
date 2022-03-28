class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sc = Counter(s)

        for tc in t:
            if tc not in sc or not sc[tc]:
                return tc
            else:
                sc[tc] -= 1
