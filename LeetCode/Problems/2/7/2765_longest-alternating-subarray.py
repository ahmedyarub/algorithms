class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        return b if (b := max(
            accumulate(pairwise(nums), lambda s, x: (s if x[0] == x[1] + (1, -1)[s % 2] else x[0] == x[1] - 1) + 1,
                       initial=1))) - 1 else -1
