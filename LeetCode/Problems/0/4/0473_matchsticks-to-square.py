class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter = sum(matchsticks)
        if perimeter < 4 or perimeter % 4:
            return False

        edge = perimeter // 4
        matchsticks.sort(reverse=True)

        @cache
        def find_edges(sides: tuple, i):
            nonlocal edge
            if i > len(matchsticks) - 1:
                return all([side == edge for side in sides])

            if any([side > edge for side in sides]):
                return False
            sides = sorted(sides)
            for s in range(4):
                sides[s] += matchsticks[i]
                if find_edges(tuple(sides), i + 1):
                    return True
                sides[s] -= matchsticks[i]

            return False

        return find_edges(tuple((0, 0, 0, 0)), 0)
