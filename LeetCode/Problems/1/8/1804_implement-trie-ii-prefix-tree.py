class TrieNode:
    def __init__(self):
        self.children = dict()
        self.cnt = 0
        self.cnt_start_with = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.cnt_start_with += 1
        node.cnt += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self.root
        for c in word:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.cnt

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.cnt_start_with

    def erase(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.children[c]
            node.cnt_start_with -= 1
        node.cnt -= 1
