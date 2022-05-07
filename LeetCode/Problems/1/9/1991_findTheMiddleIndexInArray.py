class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)

        prev = 0
        for i, n in enumerate(nums):
            right -= n

            if right == left:
                return i

            left += n

        return -1
