class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        mx, s, p = 0, 0, 0

        for num in nums:
            if num <= p:
                mx = max(mx, s)
                s = num
            else:
                s += num
                mx = max(mx, s)
            p = num

        return mx
