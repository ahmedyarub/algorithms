class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0

        stack = []  # list[(column, height)]

        for i, height in enumerate(chain([0], heights, [0])):
            while stack and stack[-1][1] > height:
                rect_right = i
                rect_height = stack.pop()[1]
                rect_left = stack[-1][0]
                area = (rect_right - rect_left - 1) * rect_height
                maxArea = max(area, maxArea)

            stack.append((i, height))

        return maxArea
