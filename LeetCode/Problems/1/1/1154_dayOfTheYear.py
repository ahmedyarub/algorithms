class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        mp, prev = {c: i for i, c in enumerate(keyboard)}, 0

        result = 0

        for c in word:
            cur = mp[c]
            result += abs(cur - prev)
            prev = cur

        return result
