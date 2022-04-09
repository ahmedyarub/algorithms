from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        target = image[sr][sc]

        if newColor == image[sr][sc]:
            return image

        queue = [[sr, sc]]

        while queue:
            r, c = queue.pop()

            if image[r][c] != target:
                continue

            image[r][c] = newColor

            if c > 0:
                queue.append([r, c - 1])

            if r > 0:
                queue.append([r - 1, c])

            if c < len(image[0]) - 1:
                queue.append([r, c + 1])

            if r < len(image) - 1:
                queue.append([r + 1, c])

        return image


if __name__ == '__main__':
    print(Solution().floodFill([[0, 0, 0], [0, 1, 1]], 1, 1, 1))
