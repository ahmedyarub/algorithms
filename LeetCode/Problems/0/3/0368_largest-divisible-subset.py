class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        subsets = {-1: set()}

        for num in sorted(nums):
            subsets[num] = max([subsets[k] for k in subsets if not num % k], key=len) | {num}

        return list(max(subsets.values(), key=len))
