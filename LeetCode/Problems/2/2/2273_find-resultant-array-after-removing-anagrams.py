class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        return [words[i] for i in range(len(words)) if not i or Counter(words[i]) != Counter(words[i - 1])]
