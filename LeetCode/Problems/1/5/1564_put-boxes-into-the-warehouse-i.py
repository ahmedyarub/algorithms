class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        bi, count = 0, 0
        boxes.sort(reverse=True)

        for w in warehouse:
            while bi < len(boxes) and boxes[bi] > w:
                bi += 1
            if bi == len(boxes):
                return count
            count += 1
            bi += 1

        return count
