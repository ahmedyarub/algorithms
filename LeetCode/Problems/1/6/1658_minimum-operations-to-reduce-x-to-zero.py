class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        s, l, left, cur, mx = sum(nums), len(nums), 0, 0, -1

        for right in range(l):
            cur += nums[right]

            while cur > s - x and left <= right:
                cur -= nums[left]
                left += 1

            if cur == s - x:
                mx = max(mx, right - left + 1)

        return l - mx if mx != -1 else -1
