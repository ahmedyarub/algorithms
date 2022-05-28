class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda w: len(w))

        result = []
        for i, word in enumerate(words):
            if any([w.find(word) >= 0 for w in words[i + 1:]]):
                result.append(word)

        return result
