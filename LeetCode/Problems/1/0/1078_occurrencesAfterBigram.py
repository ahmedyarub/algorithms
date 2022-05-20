class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        return [words[i] for i in range(2, len(words)) if words[i - 1] == second and words[i - 2] == first]
