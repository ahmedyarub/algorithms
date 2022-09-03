class Solution:
    def numsSameConsecDiff(self, n: int, k: int):
        cur = range(1, 10)
        for i in range(n - 1):
            cur = {x * 10 + y for x in cur for y in [x % 10 + k, x % 10 - k] if 0 <= y <= 9}
        return list(cur)
