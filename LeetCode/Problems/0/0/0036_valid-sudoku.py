class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_st, col_st = [set() for _ in range(9)], [set() for _ in range(9)]
        for sr in range(3):
            for cr in range(3):
                box_st = set()
                for r in range(3):
                    for c in range(3):
                        row, column = 3 * sr + r, 3 * cr + c
                        num = board[row][column]
                        if num != '.':
                            if num in box_st or num in row_st[row] or num in col_st[column]:
                                return False

                            box_st.add(num)
                            row_st[row].add(num)
                            col_st[column].add(num)

        return True
