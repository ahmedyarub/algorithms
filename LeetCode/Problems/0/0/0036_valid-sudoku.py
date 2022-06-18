class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenrow, seencol = defaultdict(set), defaultdict(set)
        for rs in range(3):
            for cs in range(3):
                seens = set()
                for row in range(rs * 3, rs * 3 + 3):
                    for col in range(cs * 3, cs * 3 + 3):
                        if board[row][col] != '.':
                            if any([board[row][col] in st for st in [seens, seenrow[row], seencol[col]]]):
                                return False

                            seens.add(board[row][col])
                            seenrow[row].add(board[row][col])
                            seencol[col].add(board[row][col])
        print(seencol)
        return True
