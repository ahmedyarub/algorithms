class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        prev, result, start = '', [], 0

        for i, c in enumerate(s + '@'):
            if c != prev:
                if i - start >= 3:
                    result.append([start, i - 1])

                prev = c
                start = i

        return result
