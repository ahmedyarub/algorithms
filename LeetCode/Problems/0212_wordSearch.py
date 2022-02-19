from typing import List


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


if __name__ == '__main__':
    print(Solution().findWords([["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]],
                               ["lllllll", "fffffff", "ssss", "s", "rr", "xxxx", "ttt", "eee", "ppppppp", "iiiiiiiii",
                                "xxxxxxxxxx", "pppppp", "xxxxxx", "yy", "jj", "ccc", "zzz", "ffffffff", "r",
                                "mmmmmmmmm", "tttttttt", "mm", "ttttt", "qqqqqqqqqq", "z", "aaaaaaaa", "nnnnnnnnn", "v",
                                "g", "ddddddd", "eeeeeeeee", "aaaaaaa", "ee", "n", "kkkkkkkkk", "ff", "qq", "vvvvv",
                                "kkkk", "e", "nnn", "ooo", "kkkkk", "o", "ooooooo", "jjj", "lll", "ssssssss", "mmmm",
                                "qqqqq", "gggggg", "rrrrrrrrrr", "iiii", "bbbbbbbbb", "aaaaaa", "hhhh", "qqq",
                                "zzzzzzzzz", "xxxxxxxxx", "ww", "iiiiiii", "pp", "vvvvvvvvvv", "eeeee", "nnnnnnn",
                                "nnnnnn", "nn", "nnnnnnnn", "wwwwwwww", "vvvvvvvv", "fffffffff", "aaa", "p", "ddd",
                                "ppppppppp", "fffff", "aaaaaaaaa", "oooooooo", "jjjj", "xxx", "zz", "hhhhh", "uuuuu",
                                "f", "ddddddddd", "zzzzzz", "cccccc", "kkkkkk", "bbbbbbbb", "hhhhhhhhhh", "uuuuuuu",
                                "cccccccccc", "jjjjj", "gg", "ppp", "ccccccccc", "rrrrrr", "c", "cccccccc", "yyyyy",
                                "uuuu", "jjjjjjjj", "bb", "hhh", "l", "u", "yyyyyy", "vvv", "mmm", "ffffff", "eeeeeee",
                                "qqqqqqq", "zzzzzzzzzz", "ggg", "zzzzzzz", "dddddddddd", "jjjjjjj", "bbbbb", "ttttttt",
                                "dddddddd", "wwwwwww", "vvvvvv", "iii", "ttttttttt", "ggggggg", "xx", "oooooo", "cc",
                                "rrrr", "qqqq", "sssssss", "oooo", "lllllllll", "ii", "tttttttttt", "uuuuuu",
                                "kkkkkkkk", "wwwwwwwwww", "pppppppppp", "uuuuuuuu", "yyyyyyy", "cccc", "ggggg", "ddddd",
                                "llllllllll", "tttt", "pppppppp", "rrrrrrr", "nnnn", "x", "yyy", "iiiiiiiiii", "iiiiii",
                                "llll", "nnnnnnnnnn", "aaaaaaaaaa", "eeeeeeeeee", "m", "uuu", "rrrrrrrr", "h", "b",
                                "vvvvvvv", "ll", "vv", "mmmmmmm", "zzzzz", "uu", "ccccccc", "xxxxxxx", "ss", "eeeeeeee",
                                "llllllll", "eeee", "y", "ppppp", "qqqqqq", "mmmmmm", "gggg", "yyyyyyyyy", "jjjjjj",
                                "rrrrr", "a", "bbbb", "ssssss", "sss", "ooooo", "ffffffffff", "kkk", "xxxxxxxx",
                                "wwwwwwwww", "w", "iiiiiiii", "ffff", "dddddd", "bbbbbb", "uuuuuuuuu", "kkkkkkk",
                                "gggggggggg", "qqqqqqqq", "vvvvvvvvv", "bbbbbbbbbb", "nnnnn", "tt", "wwww", "iiiii",
                                "hhhhhhh", "zzzzzzzz", "ssssssssss", "j", "fff", "bbbbbbb", "aaaa", "mmmmmmmmmm",
                                "jjjjjjjjjj", "sssss", "yyyyyyyy", "hh", "q", "rrrrrrrrr", "mmmmmmmm", "wwwww", "www",
                                "rrr", "lllll", "uuuuuuuuuu", "oo", "jjjjjjjjj", "dddd", "pppp", "hhhhhhhhh", "kk",
                                "gggggggg", "xxxxx", "vvvv", "d", "qqqqqqqqq", "dd", "ggggggggg", "t", "yyyy", "bbb",
                                "yyyyyyyyyy", "tttttt", "ccccc", "aa", "eeeeee", "llllll", "kkkkkkkkkk", "sssssssss",
                                "i", "hhhhhh", "oooooooooo", "wwwwww", "ooooooooo", "zzzz", "k", "hhhhhhhh", "aaaaa",
                                "mmmmm"]))
