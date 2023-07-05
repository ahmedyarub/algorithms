class Solution:
    def countDigits(self, num: int) -> int:
        cnt, n = 0, num

        while n:
            cnt += not (num%(n%10))
            n //= 10

        return cnt