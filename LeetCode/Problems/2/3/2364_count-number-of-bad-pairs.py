class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        diff_counts = defaultdict(int)
        for i, num in enumerate(nums):
            diff_counts[num - i] += 1

        return len(nums) * (len(nums) - 1) // 2 - \
               sum([diff * (diff - 1) // 2 for diff in diff_counts.values() if diff > 1])
