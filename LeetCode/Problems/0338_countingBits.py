class Solution:
    def pop_count(self, x):
        count = 0
        while x:
            x &= x - 1
            count += 1

        return count

    def countBits(self, n: int) -> List[int]:
        return [self.pop_count(i) for i in range(n + 1)]
