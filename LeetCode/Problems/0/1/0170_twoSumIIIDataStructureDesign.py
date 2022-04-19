class TwoSum:

    def __init__(self):
        self.counts = defaultdict(int)

    def add(self, number: int) -> None:
        self.counts[number] += 1

    def find(self, value: int) -> bool:
        for k in self.counts.keys():
            diff = value - k
            if diff == k:
                if self.counts[k] > 1:
                    return True
            else:
                if diff in self.counts:
                    return True

        return False
