class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hash_map and timestamp >= self.hash_map[key][0][0]:
            arr = self.hash_map[key]

            left, right = 0, len(arr)

            while left < right:
                mid = (right + left) // 2

                if arr[mid][0] > timestamp:
                    right = mid
                else:
                    left = mid + 1

            return "" if not right else arr[right - 1][1]
        else:
            return ""
