class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                adj[word[:i] + '_' + word[i + 1:]].append(word)
        visited = set()
        q = [(beginWord, 1)]
        while q:
            word, k = q.pop(0)
            if word == endWord:
                return k
            if word not in visited:
                visited.add(word)
                for i in range(len(word)):
                    neighbors = word[:i] + '_' + word[i + 1:]
                    for neighbor in adj[neighbors]:
                        q.append((neighbor, k + 1))
        return 0