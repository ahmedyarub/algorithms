from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        s = [[float('inf')] * (i + 1) for i in range(len(triangle))]

        def traverse(r: int, c: int, prev: int) -> None:
            nonlocal triangle

            cur = prev + triangle[r][c]
            if cur < s[r][c]:
                s[r][c] = cur

                if r < len(triangle) - 1:
                    traverse(r + 1, c, cur)
                    traverse(r + 1, c + 1, cur)

        traverse(0, 0, 0)

        return int(min(s[-1]))


if __name__ == '__main__':
    print(Solution().minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
