class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        return [chr(ch) + str(d) for ch in range(ord(s[0]), ord(s[- 2]) + 1) for d in range(int(s[1]), int(s[-1]) + 1)]
