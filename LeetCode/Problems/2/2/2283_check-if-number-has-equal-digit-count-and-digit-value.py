class Solution:
    def digitCount(self, num: str) -> bool:
        cnt = Counter(list(num))
        return all([cnt.get(str(i), 0) == int(c) for i, c in enumerate(list(num))])
