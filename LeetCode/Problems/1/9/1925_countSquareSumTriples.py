class Solution:
    def countTriples(self, n: int) -> int:
        result = 0

        for a in range(1, n - 1):
            for b in range(a + 1, n):
                ab = (a * a + b * b) ** 0.5
                if ab // 1 == ab and ab <= n:
                    result += 2
                elif ab > n:
                    break

        return result
