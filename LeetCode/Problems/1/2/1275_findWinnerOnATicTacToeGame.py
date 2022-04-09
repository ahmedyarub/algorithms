class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def check_win(ms):
            board = [[0] * 3 for _ in range(3)]

            for r, c in ms:
                board[r][c] = 1

            return any([sum([board[r][c] for c in range(3)]) == 3 for r in range(3)]) or \
                   any([sum([board[r][c] for r in range(3)]) == 3 for c in range(3)]) or \
                   sum([board[rc][rc] for rc in range(3)]) == 3 or \
                   sum([board[rc][2 - rc] for rc in range(3)]) == 3

        if check_win(moves[::2]):
            return 'A'

        if check_win(moves[1::2]):
            return 'B'

        return 'Draw' if len(moves) == 9 else 'Pending'
