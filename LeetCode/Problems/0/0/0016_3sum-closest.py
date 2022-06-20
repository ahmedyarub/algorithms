class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        mn = float('inf')
        nums.sort()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                complement = target - nums[i] - nums[j]
                hi = bisect_right(nums, complement, j + 1)
                lo = hi - 1

                if hi < len(nums) and abs(complement - nums[hi]) < abs(mn):
                    mn = complement - nums[hi]
                if lo > j and abs(complement - nums[lo]) < abs(mn):
                    mn = complement - nums[lo]

                if mn == 0:
                    break

        return target - mn
