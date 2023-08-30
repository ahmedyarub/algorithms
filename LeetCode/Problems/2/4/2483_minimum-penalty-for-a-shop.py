class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ry = customers.count('Y')
        mn, left, result = ry, 0, 0

        for i, c in enumerate(customers):
            if c == 'Y':
                ry -= 1
            else:
                left += 1

            penalty = left + ry

            if penalty < mn:
                mn = penalty
                result = i + 1

        return result
