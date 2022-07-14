class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.mp = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.mp[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        wis1, wis2 = self.mp[word1], self.mp[word2]
        wi1, wi2 = 0, 0
        result = float("inf")

        while wi1 < len(wis1) and wi2 < len(wis2):
            result = min(result, abs(wis1[wi1] - wis2[wi2]))
            if wis1[wi1] < wis2[wi2]:
                wi1 += 1
            else:
                wi2 += 1

        return result
