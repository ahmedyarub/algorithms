class Solution:
    def sortColors(self, nums: List[int]) -> None:
        cnt = Counter(nums)

        i = 0
        for color in range(0, 3):
            if color in cnt:
                limit = i + cnt[color]
                while i < limit:
                    nums[i] = color
                    i += 1
