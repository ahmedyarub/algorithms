class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        distance = [[-1] * len(colors) for _ in range(3)]

        for i in range(len(colors)):
            color, j = colors[i] - 1, i
            while j >= 0 and distance[color][j] == -1:
                distance[color][j] = i - j
                j -= 1

        for i in range(len(colors) - 1, -1, -1):
            color, j = colors[i] - 1, i + 1
            while j < len(colors) and (distance[color][j] == -1 or distance[color][j] > j - i):
                distance[color][j] = j - i
                j += 1

        return [distance[color - 1][index] for index, color in queries]
