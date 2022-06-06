class Solution:
    def totalMoney(self, n: int) -> int:
        days = n % 7
        weeks = n // 7
        return (days * (days + 1)) // 2 + 28 * weeks + 7 * ((weeks - 1) * weeks // 2) + weeks * days
