class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [v for v, c in Counter(s1.split() + s2.split()).items() if c == 1]
