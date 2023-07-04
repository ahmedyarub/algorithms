class Solution:
    def similarPairs(self, words: List[str]) -> int:
        dict, result = defaultdict(int), 0

        for word in words:
            key = reduce(or_, (1 << ord(ch) - ord('a') for ch in word))
            result += dict[key]
            dict[key] += 1

        return result
