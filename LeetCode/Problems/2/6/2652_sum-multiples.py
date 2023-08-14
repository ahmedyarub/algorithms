class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum([nn if any([not nn % d for d in [3, 5, 7]]) else 0 for nn in range(1, n + 1)])
