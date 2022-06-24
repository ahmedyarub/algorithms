class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        return words == [''.join(a) for a in zip_longest(*words, fillvalue='')]
