class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'X' and not (i > 0 and board[i - 1][j] == 'X') and not (
                        j > 0 and board[i][j - 1] == 'X'):
                    ans += 1

        return ans
