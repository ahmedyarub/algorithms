class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum([word[:len(pref)] == pref for word in words])
