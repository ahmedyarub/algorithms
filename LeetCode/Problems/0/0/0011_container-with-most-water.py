class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, result = 0, len(height)-1, 0

        while l < r:
            result = max(result, (r - l) * min(height[l], height[r]))
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1

        return result
