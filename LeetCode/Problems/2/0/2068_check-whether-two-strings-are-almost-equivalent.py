class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        cnt1, cnt2 = Counter(word1), Counter(word2)

        return all([abs(cn - cnt2.get(ch, 0)) <= 3 for ch, cn in cnt1.items()]) \
               and all([abs(cn - cnt1.get(ch, 0)) <= 3 for ch, cn in cnt2.items()])
