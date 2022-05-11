class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        for i in range(1, len(nums) + 1):
            if counts[i] == 0:
                missing = i
            elif counts[i] == 2:
                double = i

        return [double, missing]
