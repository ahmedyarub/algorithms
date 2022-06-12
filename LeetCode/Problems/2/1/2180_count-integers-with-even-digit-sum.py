class Solution:
    def countEven(self, num: int) -> int:
        return (num - sum([int(k) for k in str(num)]) % 2) // 2
