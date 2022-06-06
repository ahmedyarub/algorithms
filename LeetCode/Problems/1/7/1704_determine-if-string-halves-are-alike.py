class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return not sum(
            [1 if i < len(s) // 2 else -1 for i, c in enumerate(s) if c.lower() in {'a', 'e', 'i', 'o', 'u'}])
