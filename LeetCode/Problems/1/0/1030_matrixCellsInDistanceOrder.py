class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        return sorted([[r, c] for r in range(rows) for c in range(cols)],
                      key=lambda p: abs(p[0] - rCenter) + abs(p[1] - cCenter))
