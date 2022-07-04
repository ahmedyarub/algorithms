class Solution:
    def candy(self, ratings: List[int]) -> int:
        result, streak, prev, h, prev_hill = 0, 0, float('inf'), None, float('inf')

        for r in ratings:
            if r == prev:
                streak = 1
                h = False
                prev_hill = float('inf')
            elif r > prev:
                streak = 2 if not h else (streak + 1)
                prev_hill = 2 if not h else (prev_hill + 1)
                h = True
            else:
                streak = 1 if h else (streak + 1)
                h = False
                if streak >= prev_hill:
                    streak += 1
                    prev_hill = float('inf')

            result += streak
            prev = r

        return result
