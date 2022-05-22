class Solution:
    def isArmstrong(self, n: int) -> bool:
        return sum([int(d) ** len(str(n)) for d in str(n)]) == n
