class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        sh = sum([(-1 if d else 1) * v for d, v in shift]) % len(s)

        return s[sh:] + s[:sh]
