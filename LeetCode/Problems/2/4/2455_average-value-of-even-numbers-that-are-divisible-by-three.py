class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s, cnt = 0, 0

        for num in nums:
            if not num % 6:
                s += num
                cnt += 1

        return int(s / cnt) if s else 0
