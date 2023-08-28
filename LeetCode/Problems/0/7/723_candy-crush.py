class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m, n = len(board), len(board[0])

        while True:
            stable = True
            crushable = set()

            for x in range(m):
                for y in range(n - 2):
                    if board[x][y] == board[x][y + 1] == board[x][y + 2] != 0:
                        stable = False
                        crushable.update([(x, y), (x, y + 1), (x, y + 2)])

            for x in range(m - 2):
                for y in range(n):
                    if board[x][y] == board[x + 1][y] == board[x + 2][y] != 0:
                        stable = False
                        crushable.update([(x, y), (x + 1, y), (x + 2, y)])

            if stable:
                return board

            for x, y in crushable:
                board[x][y] = 0

            # 4. let the candies "fall"
            for y in range(n):
                offset = 0
                for x in range(m - 1, -1, -1):  # loop through column backward
                    k = x + offset
                    if (x, y) in crushable:
                        offset += 1
                    else:
                        board[k][y] = board[x][y]  # notice the use of k

                for x in range(offset):
                    board[x][y] = 0
