class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.RAD = radius
        self.XC = x_center
        self.YC = y_center

    def randPoint(self) -> List[float]:
        ang = random.uniform(0, 1) * 2 * math.pi
        hyp = sqrt(random.uniform(0, 1)) * self.RAD
        adj = cos(ang) * hyp
        opp = sin(ang) * hyp
        return [self.XC + adj, self.YC + opp]