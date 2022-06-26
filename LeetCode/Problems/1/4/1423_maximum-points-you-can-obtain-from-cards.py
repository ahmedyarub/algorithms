class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        arrs = sum(cardPoints[len(cardPoints) - k:])
        result = arrs

        for i in range(k):
            arrs = arrs - cardPoints[-1 * (k - i)] + cardPoints[i]
            result = max(result, arrs)

        return result
