class Solution:
    def numberOfMatches(self, n: int) -> int:
        result = 0

        while n > 1:
            result += ceil(n / 2)
            n = floor(n / 2)

        return result
