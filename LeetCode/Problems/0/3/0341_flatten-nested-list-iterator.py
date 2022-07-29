class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = deque(nestedList)

    def next(self) -> int:
        return self.queue.popleft().getInteger()

    def hasNext(self) -> bool:
        while self.queue:
            if self.queue[0].isInteger():
                return True
            first = self.queue.popleft()
            self.queue.extendleft(first.getList()[::-1])
        return False
