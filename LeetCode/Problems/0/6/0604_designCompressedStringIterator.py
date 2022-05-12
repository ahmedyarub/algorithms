class StringIterator:

    def __init__(self, compressedString: str):
        self.__data = re.findall(r"([a-zA-Z])(\d+)", compressedString)
        self.__index, self.__count = -1, 0

    def next(self) -> str:
        if self.hasNext():
            self.__count -= 1
            return self.__data[self.__index][0]
        else:
            return ' '

    def hasNext(self) -> bool:
        if self.__count == 0 and self.__index + 1 < len(self.__data):
            self.__index += 1
            self.__count = int(self.__data[self.__index][1])
        return self.__count > 0

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
