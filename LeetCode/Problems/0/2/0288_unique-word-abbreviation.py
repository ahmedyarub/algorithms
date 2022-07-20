class ValidWordAbbr:

    def __init__(self, dictionary):
        self.dt = collections.defaultdict(set)
        for d in dictionary:
            self.dt[d[0], len(d), d[-1]].add(d)

    def isUnique(self, word):
        return self.dt[word[0], len(word), word[-1]] <= {word}
