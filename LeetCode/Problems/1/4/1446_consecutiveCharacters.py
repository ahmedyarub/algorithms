class Solution:
    def maxPower(self, s: str) -> int:
        cur_count = max_count = 1
        last = None

        for c in s:
            if c == last:
                cur_count += 1
                max_count = max(max_count, cur_count)
            else:
                last = c
                cur_count = 1

        return max_count
