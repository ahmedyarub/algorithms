class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        st, cur, result, left = set(), 0, 0, 0

        for n in nums:
            while n in st:
                cur -= nums[left]
                st.remove(nums[left])
                left += 1

            st.add(n)
            cur += n
            result = max(result, cur)

        return result
