class Solution:
    def oddString(self, words: List[str]) -> str:
        hashmap = defaultdict(list)
        for w in words:
            hashmap[reduce(lambda d, i: d * 26 + ord(w[i + 1]) - ord(w[i]), range(len(w) - 1), 0)].append(w)

        for ws in hashmap.values():
            if len(ws) == 1:
                return ws[0]
