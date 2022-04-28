class Solution:
    def balancedStringSplit(self, s: str) -> int:
        w_count = d_count = 0
        for ch in s:
            if ch == "L":
                d_count += 1
            else:
                d_count -= 1
            if not d_count:
                w_count += 1
        return w_count