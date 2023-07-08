class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum1, sum2 = 0, 0

        for num in nums:
            sum2 += num

            while num:
                sum1 += num % 10
                num //= 10

        return sum2 - sum1
