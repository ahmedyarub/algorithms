class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        cur = self.trie

        for c in list(word):
            if c not in cur:
                cur[c] = {}

            cur = cur[c]

        cur['#'] = word

    def search(self, word: str) -> bool:
        def scan(wi: int, cur: dict) -> bool:
            if wi == len(word):
                return '#' in cur

            c = word[wi]
            if c == '.':
                return any([scan(wi + 1, nc) for nk, nc in cur.items() if nk != '#'])
            else:
                return c in cur and scan(wi + 1, cur[c])

        return scan(0, self.trie)
