class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        st1, st2, st3 = set(nums1), set(nums2), set(nums3)
        return list(set.union(st1 & st2, st1 & st3, st2 & st3))
