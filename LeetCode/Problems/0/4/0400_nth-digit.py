class Solution:
    def findNthDigit(self, n: int) -> int:
        if n <= 9:
            return n

        digits = 0
        cur_sum = prev_sum = 9
        for i in range(2, 11):
            cur_sum = cur_sum + (9 * i * pow(10, i - 1))
            if n <= cur_sum:
                digits = i
                break
            prev_sum = cur_sum

        res = ceil((n - prev_sum) / digits) + int('9' * (digits - 1))
        return int(str(res)[(n - prev_sum) % digits - 1])
