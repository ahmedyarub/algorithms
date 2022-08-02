class HitCounter:

    def __init__(self):
        self.queue, self.cnt = [], 0

    def hit(self, timestamp: int) -> None:
        self.cnt += 1
        self.queue.append((timestamp, self.cnt))

    def getHits(self, timestamp: int) -> int:
        while self.queue and self.queue[0][0] <= timestamp - 300:
            self.queue.pop(0)

        return (self.queue[-1][1] - self.queue[0][1] + 1) if self.queue else 0
