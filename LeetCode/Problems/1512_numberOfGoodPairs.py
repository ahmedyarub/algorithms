class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        found = dict()
        counter = 0
        for _, num in enumerate(nums):
            if num in found:
                counter += found[num]
                found[num] += 1
            else:
                found[num] = 1

        return counter
