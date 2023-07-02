class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max(int(s) if s.isnumeric() else len(s) for s in strs)
