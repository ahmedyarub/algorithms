class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        height, width = len(img), len(img[0])
        result = [[None] * width for _ in range(height)]

        for r in range(height):
            for c in range(width):
                cells = [[n for n in row[max(0, c - 1):min(width, c + 2)]] for row in
                         img[max(0, r - 1):min(height, r + 2)]]
                result[r][c] = sum([sum(row) for row in cells]) // (len(cells) * len(cells[0]))

        return result
