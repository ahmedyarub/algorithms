class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        return len([num for num in nums if num == target]) > len(nums) // 2
