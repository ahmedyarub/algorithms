class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        I, J = divmod(sum(board, []).index('R'), 8)
        C = "".join([i for i in [board[I] + ['B'] + [board[i][J] for i in range(8)]][0] if i != '.'])
        return C.count('Rp') + C.count('pR')
