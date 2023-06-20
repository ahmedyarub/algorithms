class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        @cache
        def traverse(curr: int, idx: int) -> bool:
            nonlocal s

            if idx == len(nums):
                return curr == s // 2
            elif curr + nums[idx] == s // 2 or (curr + nums[idx] < s // 2 and traverse(curr + nums[idx], idx + 1)):
                return True
            else:
                return traverse(curr, idx + 1)

        return not s % 2 and traverse(0, 0)
