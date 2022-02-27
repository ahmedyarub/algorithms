class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = len(nums1) - 1
        m -= 1
        n -= 1
        while i >= 0:
            if m >= 0 and (n < 0 or nums1[m] > nums2[n]):
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1

            i -= 1