class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        dist, i1, i2 = float('inf'), float('inf'), float('inf')

        for i, word in enumerate(wordsDict):
            if word == word1:
                i1 = i
            elif word == word2:
                i2 = i

            if i1 != -1 and i2 != -1:
                dist = min(dist, abs(i2 - i1))

        return dist
