class WordFilter:

    def __init__(self, words: List[str]):
        self.pref, self.suff = defaultdict(set), defaultdict(set)
        self.mem = dict()

        for i, word in enumerate(words):
            for j in range(len(word)):
                self.pref[word[:j + 1]].add(i)
                self.suff[word[-1 * j - 1:]].add(i)

    def f(self, prefix: str, suffix: str) -> int:
        key = (prefix, suffix)

        if key not in self.mem:
            self.mem[key] = max(self.pref[prefix] & self.suff[suffix], default=-1)

        return self.mem[key]
