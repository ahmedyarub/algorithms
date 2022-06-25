class Solution:
    def countAsterisks(self, s: str) -> int:
        return sum([word.count('*') for word in s.split('|')[0::2]])
