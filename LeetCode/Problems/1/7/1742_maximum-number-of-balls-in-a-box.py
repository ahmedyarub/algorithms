class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        return max(Counter([sum([int(c) for c in str(n)]) for n in range(lowLimit, highLimit + 1)]).values())
