class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letters = [c.lower() for c in licensePlate if c.isalpha()]

        result = None

        for word in words:
            if all(letters.count(letters[i]) <= word.count(letters[i]) for i in range(len(letters))):
                if not result or len(result) > len(word):
                    result = word

        return result
