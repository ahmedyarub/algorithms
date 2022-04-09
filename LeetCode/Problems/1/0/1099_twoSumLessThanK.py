class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        count = [0] * 1001
        for num in nums:
            count[num] += 1

        result = -1

        left, right = 0, 1000

        while left <= right:
            if not count[right] or left + right >= k:
                right -= 1
            else:
                if count[left] > (0 if left < right else 1):
                    result = max(result, left + right)
                left += 1

        return result
