class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        return len(
            set([word for word, cnt in Counter(words1).items() if cnt == 1])
            & set([word for word, cnt in Counter(words2).items() if cnt == 1])
        )
