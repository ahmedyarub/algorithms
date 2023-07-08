class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i1, i2 = 0, 0

        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] == nums2[i2]:
                return nums1[i1]
            elif nums1[i1] > nums2[i2]:
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                i1 += 1

        return -1
