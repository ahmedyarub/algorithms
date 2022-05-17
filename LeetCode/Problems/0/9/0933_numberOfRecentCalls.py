class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)

        for i, r in enumerate(self.requests):
            if r >= t - 3000:
                break

        self.requests = self.requests[i:]

        return len(self.requests)
