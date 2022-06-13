class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        st1, st2 = set(nums1), set(nums2)
        return [list(st1 - st2), list(st2 - st1)]
