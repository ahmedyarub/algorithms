class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter([c for c in s])

        return min(count.values()) == max(count.values())
