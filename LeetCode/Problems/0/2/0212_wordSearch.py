class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        found_words = set()

        trie = build_trie(words)

        for i in range(len(board)):
            for j in range(len(board[0])):
                backtracking(board, i, j, trie, found_words, set())

        return list(found_words)


def backtracking(board, x, y, parent, found_words, known_coords):
    known_coords.add(tuple([x, y]))

    cur_char = board[x][y]
    if cur_char not in parent:
        return

    node = parent[cur_char]

    for coord in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
        next_x = x + coord[0]
        next_y = y + coord[1]

        if tuple([next_x, next_y]) not in known_coords and 0 <= next_x < len(board) and 0 <= next_y < len(board[0]):
            backtracking(board, next_x, next_y, node, found_words, known_coords.copy())

    if "$" in node:
        found_words.add(node.pop("$"))

    if not node:
        parent.pop(cur_char)


def build_trie(words):
    trie = {}

    for word in words:
        node = trie
        for char in word:
            if char not in node:
                node[char] = {}

            node = node[char]

        node["$"] = word

    return trie
