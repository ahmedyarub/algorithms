class MedianFinder:

    def __init__(self):
        self.upper_heap = []
        self.lower_heap = []

    def addNum(self, num: int) -> None:
        if not len(self.upper_heap) or num > self.upper_heap[0]:
            if len(self.upper_heap) <= len(self.lower_heap):
                heappush(self.upper_heap, num)
            else:
                heappush(self.lower_heap, -1 * heappushpop(self.upper_heap, num))
        else:
            if len(self.lower_heap) <= len(self.upper_heap):
                heappush(self.lower_heap, -1 * num)
            else:
                heappush(self.upper_heap, heappushpop(self.lower_heap, -1 * num) * -1)

    def findMedian(self) -> float:
        if len(self.lower_heap) > len(self.upper_heap):
            return self.lower_heap[0] * -1
        elif len(self.lower_heap) < len(self.upper_heap):
            return self.upper_heap[0]
        else:
            return ((self.lower_heap[0] * -1) + self.upper_heap[0]) / 2
