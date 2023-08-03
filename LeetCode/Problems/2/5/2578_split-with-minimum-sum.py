class Solution:
    def splitNum(self, num: int) -> int:
        digits, n1, n2, cond = sorted([int(d) for d in str(num)]), 0, 0, True

        for d in digits:
            if cond:
                n1 = n1 * 10 + d
            else:
                n2 = n2 * 10 + d

            cond = not cond

        return n1 + n2
