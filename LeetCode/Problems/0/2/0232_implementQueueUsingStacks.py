class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.front = None

    def push(self, x: int) -> None:
        if not self.stack1:
            self.front = x

        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        else:
            return self.front

    def empty(self) -> bool:
        return not len(self.stack1) and not len(self.stack2)
