class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        cnt2 = reduce(lambda cnt, word2: cnt | Counter(word2), words2, Counter())
        return [pair[0] for pair in [(word1, Counter(word1)) for word1 in words1]
                if all([key2 in pair[1] and pair[1][key2] >= cnt2[key2] for key2 in cnt2.keys()])]
