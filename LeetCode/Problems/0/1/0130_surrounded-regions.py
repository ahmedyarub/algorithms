class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                cur = board[row][col]
                if cur == 'O' and cur not in visited:
                    region, queue, surrounded = set(), [(row, col)], True

                    while queue:
                        crow, ccol = queue.pop()

                        if crow >= 0 and crow < len(board) and ccol >= 0 and ccol < len(board[0]) \
                                and board[crow][ccol] == 'O' and (crow, ccol) not in region:

                            region.add((crow, ccol))
                            if crow == 0 or crow == len(board) - 1 or ccol == 0 or ccol == len(board[0]) - 1:
                                surrounded = False

                            queue.extend([(crow, ccol - 1), (crow - 1, ccol), (crow, ccol + 1), (crow + 1, ccol)])

                    if surrounded:
                        for rrow, rcol in region:
                            board[rrow][rcol] = "X"

                    visited.update(region)
