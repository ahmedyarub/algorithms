class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = [0]

        for i, h in enumerate(heights[1:]):
            while stack and h >= heights[stack[-1]]:
                stack.pop()

            stack.append(i + 1)

        return stack
