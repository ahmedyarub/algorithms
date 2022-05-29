class Solution:
    def maxProduct(self, words: List[str]) -> int:
        sets = list(map(set, words))

        result = 0
        for i in range(len(sets) - 1):
            for j in range(i + 1, len(sets)):
                if all([c not in sets[j] for c in sets[i]]):
                    result = max(result, len(words[i]) * len(words[j]))

        return result
