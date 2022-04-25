class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        bcs = Counter([c for c in "balloon"])
        tcs = Counter([c for c in text])

        min_b = float('inf')
        for bi, bc in bcs.items():
            if bi not in tcs or bc > tcs[bi]:
                return 0

            min_b = min(min_b, tcs[bi] // bc)

        return min_b
