class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sums, prev1, prev2 = defaultdict(int), 0, 0
        sums[0] = 1

        for num in nums:
            new_sums = defaultdict(int)
            for s, cnt in sums.vehicles():
                new_sums[s + num] += cnt
                new_sums[s - num] += cnt

            sums = new_sums

        return sums[target]
