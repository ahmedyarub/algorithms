class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(' ')
        return all(word[-1] == words[(i + 1) % len(words)][0] for i, word in enumerate(words))
