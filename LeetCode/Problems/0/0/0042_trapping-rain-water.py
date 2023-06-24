class Solution:
    def trap(self, height: List[int]) -> int:
        left, right, mx_left, mx_right, result = 0, len(height) - 1, float('-inf'), float('-inf'), 0

        while left < right:
            if height[left] < height[right]:
                if height[left] > mx_left:
                    mx_left = height[left]
                else:
                    result += mx_left - height[left]
                left += 1
            else:
                if height[right] > mx_right:
                    mx_right = height[right]
                else:
                    result += mx_right - height[right]
                right -= 1

        return result
