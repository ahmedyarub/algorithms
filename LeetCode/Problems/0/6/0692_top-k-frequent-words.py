class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mp = defaultdict(list)
        for word, cnt in Counter(words).items():
            mp[cnt].append(word)

        hp = []

        for key in mp.keys():
            for word in mp[key]:
                heappush(hp, [-1 * key, word])

        return [heappop(hp)[1] for _ in range(k)]