class Solution:
    def getMoneyAmount(self, n: int) -> int:
        need = [[0] * (n + 1) for _ in range(n + 1)]
        for lo in range(n, 0, -1):
            for hi in range(lo + 1, n + 1):
                need[lo][hi] = min(x + max(need[lo][x - 1], need[x + 1][hi])
                                   for x in range(lo, hi))
        return need[1][n]
