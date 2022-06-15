from typing import List


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


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
