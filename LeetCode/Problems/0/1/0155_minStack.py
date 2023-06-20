class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minn = val if not self.stack else min(self.stack[-1][1], val)
        self.stack.append([val, minn])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
