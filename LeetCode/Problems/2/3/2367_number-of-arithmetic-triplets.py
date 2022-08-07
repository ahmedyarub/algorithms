class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        st = set(nums)

        return sum([num + diff in st and num + diff * 2 in st for num in nums[:len(nums) - 2]])
