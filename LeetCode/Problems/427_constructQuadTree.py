"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        width = len(grid)
        node_average = sum(sum(grid, [])) / (width ** 2)

        if node_average == 0 or node_average == 1:
            return Node(int(node_average), 1, None, None, None, None)
        else:
            return Node(1, 0,
                        self.construct([grid[i][0:width // 2] for i in range(0, width // 2)]),
                        self.construct([grid[i][width // 2:width] for i in range(0, width // 2)]),
                        self.construct([grid[i][0:width // 2] for i in range(width // 2, width)]),
                        self.construct([grid[i][width // 2:width] for i in range(width // 2, width)])
                        )
