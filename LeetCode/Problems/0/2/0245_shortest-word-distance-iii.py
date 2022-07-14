class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        result, last_w1, last_w2 = float("inf"), float("-inf"), float("-inf")

        for i, word in enumerate(wordsDict):
            if word == word1 and (word1 != word2 or last_w1 < last_w2):
                last_w1 = i
            elif word == word2:
                last_w2 = i

            result = min(result, abs(last_w1 - last_w2))

        return result
