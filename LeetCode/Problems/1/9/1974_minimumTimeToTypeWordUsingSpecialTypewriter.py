class Solution:
    def minTimeToType(self, word: str) -> int:
        count, cur = 0, 'a'

        for c in word:
            cost = abs(ord(cur) - ord(c))
            count += min(cost, 26 - cost)
            cur = c

        return count + len(word)
