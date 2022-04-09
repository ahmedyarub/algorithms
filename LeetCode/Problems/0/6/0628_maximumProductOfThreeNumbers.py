class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1, max2, max3, min1, min2 = float('-Inf'), float('-Inf'), float('-Inf'), float('Inf'), float('Inf')
        for num in nums:
            if num >= max1:
                max3, max2, max1 = max2, max1, num
            elif num >= max2:
                max3, max2 = max2, num
            elif num > max3:
                max3 = num
            if num <= min1:
                min2, min1 = min1, num
            elif num < min2:
                min2 = num

        return max(max1 * max2 * max3, min1 * min2 * max1)
