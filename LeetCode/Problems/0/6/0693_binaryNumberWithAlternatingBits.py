class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n, cur = divmod(n, 2)
        while n:
            if cur == n % 2:
                return False

            n, cur = divmod(n, 2)

        return True
