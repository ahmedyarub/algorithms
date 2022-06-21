class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        jumps_pq = []
        for i in range(len(heights) - 1):
            jump_height = heights[i + 1] - heights[i]
            if jump_height <= 0:
                continue
            heappush(jumps_pq, jump_height)
            if len(jumps_pq) > ladders:
                bricks -= heappop(jumps_pq)
            if bricks < 0:
                return i
        return len(heights) - 1
