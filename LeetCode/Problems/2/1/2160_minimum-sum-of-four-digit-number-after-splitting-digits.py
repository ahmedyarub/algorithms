class Solution:
    def minimumSum(self, num: int) -> int:
        n1, n2 = 0, 0
        digits = sorted(map(int, list(str(num))))

        for i in range(0, len(digits), 2):
            n1 = n1 * 10 + digits[i]

            if i + 1 < len(digits):
                n2 = n2 * 10 + digits[i + 1]

        return n1 + n2
