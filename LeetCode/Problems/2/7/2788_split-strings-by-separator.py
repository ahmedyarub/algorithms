class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return [word for split_words in [w.split(separator) for w in words] for word in split_words if word]
