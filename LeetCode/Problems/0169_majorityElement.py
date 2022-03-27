class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if not count:
                candidate = num

            count += (1 if candidate == num else -1)

        return candidate
