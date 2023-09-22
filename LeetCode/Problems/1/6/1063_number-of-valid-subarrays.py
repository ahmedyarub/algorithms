class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        result, st = 0, []

        for i in range(len(nums)):
            while st and nums[i] <= nums[st[-1]]:
                result += i - st.pop()

            st.append(i)

        while st:
            result += len(nums) - st.pop()

        return result
