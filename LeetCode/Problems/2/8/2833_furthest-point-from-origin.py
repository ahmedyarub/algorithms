class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        result, r, l, underscore = 0, 0, 0, 0

        for move in moves:
            if move == 'R':
                r += 1
            elif move == 'L':
                l += 1
            else:
                underscore += 1

        return abs(r - l) + underscore
