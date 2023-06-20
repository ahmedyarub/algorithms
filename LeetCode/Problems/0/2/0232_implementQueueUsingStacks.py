class MyQueue:
    def __init__(self):
        self.stack1, self.stack2 = [], []

    def push(self, x: int) -> None:
        if len(self.stack2):
            while len(self.stack2):
                self.stack1.append(self.stack2.pop())

        self.stack1.append(x)

    def pop(self) -> int:
        if len(self.stack1):
            while len(self.stack1):
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self) -> int:
        if len(self.stack1):
            while len(self.stack1):
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def empty(self) -> bool:
        return not (len(self.stack1) or len(self.stack2))
