class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        return next([a, n - a] for a in range(n) if '0' not in str(a) + str(n - a))
