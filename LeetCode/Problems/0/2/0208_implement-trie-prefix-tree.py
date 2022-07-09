class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        cur = self.trie

        for c in list(word):
            if c not in cur:
                cur[c] = {}

            cur = cur[c]

        cur['#'] = word

    def search(self, word: str) -> bool:
        cur = self.trie

        for c in list(word):
            if c not in cur:
                return False

            cur = cur[c]

        return '#' in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie

        for c in list(prefix):
            if c not in cur:
                return False

            cur = cur[c]

        return True
