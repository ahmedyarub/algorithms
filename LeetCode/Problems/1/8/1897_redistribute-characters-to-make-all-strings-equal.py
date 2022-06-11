class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        return all([not c % len(words) for c in Counter(list("".join(words))).values()])
