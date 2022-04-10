class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        direction = None

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]

            if diff:
                if not direction:
                    direction = diff
                elif (diff > 0 and direction < 0) or (diff < 0 and direction > 0):
                    return False

        return True
