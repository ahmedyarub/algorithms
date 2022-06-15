class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        cnt, result = Counter(nums), set()

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                rem = 0 - (nums[i] + nums[j])
                if rem in cnt and cnt[rem] >= ([nums[i], nums[j]].count(rem) + 1):
                    result.add(tuple(sorted([nums[i], nums[j], rem])))

        return list(map(list, result))
