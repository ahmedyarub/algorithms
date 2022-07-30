class TicTacToe:

    def __init__(self, n: int):
        self.ln = n
        self.count = Counter()

    def move(self, row: int, col: int, player: int) -> int:
        for i, x in enumerate((row, col, row + col, row - col)):
            self.count[i, x, player] += 1
            if self.count[i, x, player] == self.ln:
                return player
        return 0
