class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        target = image[sr][sc]

        def driver(r, c):
            if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == target:
                image[r][c] = color

                driver(r - 1, c)
                driver(r + 1, c)
                driver(r, c - 1)
                driver(r, c + 1)

        if target != color:
            driver(sr, sc)

        return image
