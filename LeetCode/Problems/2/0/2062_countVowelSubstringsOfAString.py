class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        return sum(set(word[i:j + 1]) == set('aeiou') for i in range(len(word) - 4) for j in range(i + 4, len(word)))
