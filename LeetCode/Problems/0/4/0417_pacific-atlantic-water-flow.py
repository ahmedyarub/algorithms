class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []

        num_rows, num_cols = len(matrix), len(matrix[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(row: int, col: int, reachable: set):
            reachable.add((row, col))
            for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_row, new_col = row + x, col + y

                if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
                    continue

                if (new_row, new_col) not in reachable and matrix[new_row][new_col] >= matrix[row][col]:
                    dfs(new_row, new_col, reachable)

        for i in range(num_rows):
            dfs(i, 0, pacific_reachable)
            dfs(i, num_cols - 1, atlantic_reachable)
        for i in range(num_cols):
            dfs(0, i, pacific_reachable)
            dfs(num_rows - 1, i, atlantic_reachable)

        return list(pacific_reachable.intersection(atlantic_reachable))
