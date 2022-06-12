class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev, result = float('-inf'), 0

        for n in [int(word) for word in s.split() if word.isnumeric()]:
            if n <= prev:
                return False
            prev = n

        return True
