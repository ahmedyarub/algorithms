class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects

        self.weights = [(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rects]
        sum_of_weights = sum(self.weights)

        self.weights = [x / sum_of_weights for x in self.weights]

    def pick(self) -> List[int]:
        rect = random.choices(population=self.rects, weights=self.weights, k=1)[0]

        x1, y1, x2, y2 = rect

        rnd_x = random.randint(x1, x2)
        rnd_y = random.randint(y1, y2)
        return [rnd_x, rnd_y]
