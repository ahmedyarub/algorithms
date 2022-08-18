class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        cnts = defaultdict(int)
        streak = 0
        for i in range(len(p)):
            streak = (streak + 1) if (ord(p[i - 1]) - 96) % 26 == (ord(p[i]) - 97) else 1
            cnts[p[i]] = max(cnts[p[i]], streak)
        return sum(cnts.values())