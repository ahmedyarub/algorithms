class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        st1, st2 = set(nums1), set(nums2)
        inter = st1.intersection(st2)

        if inter:
            return min(inter)
        else:
            min1, min2 = min(nums1), min(nums2)
            return min(min1, min2) * 10 + max(min1, min2)
