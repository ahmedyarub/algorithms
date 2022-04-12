class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = nums[:k]
        self.k = k

        heapify(self.h)

        for i in range(k, len(nums)):
            self.add(nums[i])

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heappush(self.h, val)
        elif self.h[0] < val:
            heappop(self.h)
            heappush(self.h, val)

        return self.h[0]
