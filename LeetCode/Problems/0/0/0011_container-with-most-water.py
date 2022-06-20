class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, result = 0, len(height) - 1, 0

        while left < right:
            result = max(result, (right - left) * min(height[left], height[right]))

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return result
