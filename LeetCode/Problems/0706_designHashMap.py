class MyHashMap:

    def __init__(self):
        self.map = [[] for _ in range(10)]

    def put(self, key: int, value: int) -> None:
        l = self.map[key % 10]
        for i in range(len(l)):
            if key == l[i][0]:
                l[i][1] = value
                return

        l.append([key, value])

    def get(self, key: int) -> int:
        l = self.map[key % 10]
        for k, v in l:
            if key == k:
                return v

        return -1

    def remove(self, key: int) -> None:
        l = self.map[key % 10]
        for i in range(len(l)):
            if key == l[i][0]:
                del l[i]
                return
