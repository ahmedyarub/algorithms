class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited, prev = {(0, 0), }, (0, 0)

        for d in path:
            match d:
                case 'N':
                    p = (prev[0], prev[1] + 1)
                case 'E':
                    p = (prev[0] + 1, prev[1])
                case 'S':
                    p = (prev[0], prev[1] - 1)
                case 'W':
                    p = (prev[0] - 1, prev[1])

            if p in visited:
                return True

            visited.add(p)
            prev = p

        return False
