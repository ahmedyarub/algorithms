class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()

        for s, e in ranges:
            if s <= left <= e:
                if s <= right <= e:
                    return True
                else:
                    left = e + 1

        return False
