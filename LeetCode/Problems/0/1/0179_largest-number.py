class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from numpy import sign
        def comparator(s1, s2):
            return

        nums = sorted(map(str, nums), key=cmp_to_key(comparator), reverse=True)
        return '0' if nums[0] == '0' else ''.join(nums)
