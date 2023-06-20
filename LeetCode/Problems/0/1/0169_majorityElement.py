class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = defaultdict(int)

        for num in nums:
            cnt[num] += 1
            if cnt[num] > len(nums) // 2:
                return num
