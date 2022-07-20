class Solution:
    def wallsAndGates(self, rooms):
        q = [(i, j) for i, row in enumerate(rooms) for j, r in enumerate(row) if not r]
        for i, j in q:
            for I, J in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= I < len(rooms) and 0 <= J < len(rooms[0]) and rooms[I][J] > 2 ** 30:
                    rooms[I][J] = rooms[i][j] + 1
                    q += (I, J),
