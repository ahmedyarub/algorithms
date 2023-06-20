class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtracking(i, j, wi):
            nonlocal word, board
            print(word[wi:] + ': ' + str(i) + ',' + str(j))
            if wi == len(word):
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
                return False

            if board[i][j] == word[wi]:
                board[i][j] = "~"
                if backtracking(i + 1, j, wi + 1) or \
                        backtracking(i - 1, j, wi + 1) or \
                        backtracking(i, j + 1, wi + 1) or \
                        backtracking(i, j - 1, wi + 1):
                    return True

                board[i][j] = word[wi]
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if backtracking(i, j, 0):
                    return True
        return False
