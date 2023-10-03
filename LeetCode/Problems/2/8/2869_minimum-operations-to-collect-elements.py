class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        st, cnt = set(), 0
        for num in nums[::-1]:
            cnt += 1
            if 0 < num <= k:
                st.add(num)

            if len(st) == k:
                return cnt
