class Solution:
    def jump(self, nums: List[int]) -> int:
        mx, i, cnt = max(nums), len(nums) - 1, 0

        while i:
            j = max(0, i - mx)
            while j + nums[j] < i:
                j += 1

            i = j
            cnt += 1

        return cnt
