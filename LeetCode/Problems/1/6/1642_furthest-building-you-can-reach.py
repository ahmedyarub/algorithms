class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        result = 0

        def traverse(bricks: int, ladders: int, start: int):
            nonlocal result, heights
            if bricks < 0 or ladders < 0:
                result = max(result, start - 1)
                return

            if start == len(heights) - 1:
                result = max(result, start)
                return

            diff = heights[start + 1] - heights[start]

            if diff > 0:
                traverse(bricks, ladders - 1, start + 1)
                traverse(bricks - diff, ladders, start + 1)
            else:
                traverse(bricks, ladders, start + 1)

        traverse(bricks, ladders, 0)

        return result
