class Solution:
    def integerReplacement(self, n: int) -> int:
        cnt = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
            cnt += 1

        return cnt
