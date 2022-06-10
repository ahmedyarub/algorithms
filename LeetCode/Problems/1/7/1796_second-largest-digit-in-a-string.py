class Solution:
    def secondHighest(self, s: str) -> int:
        return ([-1, -1] + sorted(list({int(c) for c in s if c.isnumeric()})))[-2]
