class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        st = set(list(brokenLetters))

        return sum([all([c not in st for c in word]) for word in text.split()])
