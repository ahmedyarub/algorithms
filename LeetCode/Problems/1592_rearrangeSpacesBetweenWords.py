class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        spaces = len(text) - sum([len(word) for word in words])
        separator = (" " * (spaces // (len(words) - 1))) if len(words) > 1 else ""

        result = separator.join(words)
        return result + " " * (len(text) - len(result))
