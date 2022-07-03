class Solution:
    def wiggleMaxLength(self, nums):
        norep = [num for num, _ in itertools.groupby(nums)]

        if len(norep) < 2:
            return len(norep)

        return 2 + sum(a < b > c or a > b < c for a, b, c in zip(norep, norep[1:], norep[2:]))
