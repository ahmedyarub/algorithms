class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        if a > b:
            a, b = b, a

        cnt, f = 1 + (b > 1 and b % a == 0), a // 2

        while f > 1:
            cnt += (not a % f) and (not b % f)
            f -= 1

        return cnt
