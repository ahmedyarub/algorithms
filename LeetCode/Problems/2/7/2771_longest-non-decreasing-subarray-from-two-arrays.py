class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        ans, s0, s1 = 1, 1, 1

        for a1, b1, a2, b2 in zip(nums1, nums1[1:],
                                  nums2, nums2[1:]):
            s0, s1 = (max(s0 * (a1 <= b1), s1 * (a2 <= b1)) + 1,
                      max(s0 * (a1 <= b2), s1 * (a2 <= b2)) + 1)

            ans = max(ans, s0, s1)

        return ans
