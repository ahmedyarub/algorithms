class Logger:

    def __init__(self):
        self.last_printed = dict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.last_printed and self.last_printed[message] + 10 > timestamp:
            return False

        self.last_printed[message] = timestamp
        return True
