class MyStack:

    def __init__(self):
        self.q1, self.q2 = deque(), deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        result = self.q1.popleft()

        self.q1, self.q2 = self.q2, self.q1

        return result

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        result = self.q1.popleft()
        self.q2.append(result)

        self.q1, self.q2 = self.q2, self.q1

        return result

    def empty(self) -> bool:
        return not self.q1
