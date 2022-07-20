class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                cur = board[row][col]

                neighbors = sum([board[r][c] >= 1 if row != r or col != c else 0
                                 for r in range(max(row - 1, 0), min(row + 2, len(board)))
                                 for c in range(max(col - 1, 0), min(col + 2, len(board[0])))
                                 ])

                if cur == 1:
                    if 2 > neighbors or neighbors > 3:
                        board[row][col] = 2
                elif neighbors == 3:
                    board[row][col] = 0.5

        for row in range(len(board)):
            for col in range(len(board[0])):
                cur = board[row][col]
                if cur == 2:
                    board[row][col] = 0
                elif cur == 0.5:
                    board[row][col] = 1
