class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        return [s[i:min(i + k, len(s))] + fill * (0 if i + k - 1 < len(s) else i + k - len(s))
                for i in range(0, len(s), k)]
