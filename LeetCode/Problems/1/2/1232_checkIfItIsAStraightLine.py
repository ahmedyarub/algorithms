def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    dy = y1 - y0
    dx = x1 - x0
    xp = dx * y0 - dy * x0  # See analysis below

    for x, y in coordinates:
        if dx * y - dy * x != xp:
            return False
    else:
        return True
