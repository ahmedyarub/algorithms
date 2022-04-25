class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        prev = 0
        for num in nums:
            result.append(prev + num)
            prev = prev + num

        return result
