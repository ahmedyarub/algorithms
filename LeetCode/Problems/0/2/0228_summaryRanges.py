class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        def create_string(a, b):
            return str(f) + ('->' + str(t) if f != t else '')

        f = nums[0]
        t = nums[0]

        result = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != 1:
                result.append(create_string(f, t))
                f = nums[i]

            t = nums[i]

        result.append(create_string(f, t))

        return result
