class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def traverse(r: int, c: int, word: str):
            nonlocal visited
            if len(board) > r >= 0 and len(board[0]) > c >= 0 and (r, c) not in visited and board[r][c] == word[0]:
                if len(word) == 1:
                    return True

                visited.add((r, c))
                result = any([traverse(row, col, word[1:]) for row, col in
                              [(r + 1, c), (r, c - 1), (r - 1, c), (r, c + 1)]])
                visited.remove((r, c))

                return result

        return any([traverse(row, col, word) for row in range(len(board)) for col in range(len(board[0]))
                    if board[row][col] == word[0]])
