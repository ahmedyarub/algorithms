class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        st = set()

        for i in range(len(nums) - 1):
            cur = nums[i] + nums[i + 1]
            if cur in st:
                return True
            else:
                st.add(cur)

        return False
