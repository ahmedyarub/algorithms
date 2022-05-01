class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [nums[0]]

        for num in nums[1:]:
            self.sums.append(self.sums[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right] - (0 if not left else self.sums[left - 1])
