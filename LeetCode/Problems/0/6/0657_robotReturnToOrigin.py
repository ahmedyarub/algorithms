class Solution:
    def judgeCircle(self, moves: str) -> bool:
        mvs = {
            "U": [0, 1],
            "D": [0, -1],
            "L": [-1, 0],
            "R": [1, 0]
        }

        start = [0, 0]
        for move in moves:
            start[0] += mvs[move][0]
            start[1] += mvs[move][1]

        return not start[0] and not start[1]
