class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        count = Counter(str(n))
        return any(count == Counter(str(1 << b)) for b in range(31))
