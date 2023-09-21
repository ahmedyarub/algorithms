class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        na, nb = len(nums1), len(nums2)
        n = na + nb

        def solve(k, a_start, a_end, b_start, b_end):
            if a_start > a_end:
                return nums2[k - a_start]
            if b_start > b_end:
                return nums1[k - b_start]

            a_index, b_index = (a_start + a_end) // 2, (b_start + b_end) // 2
            a_value, b_value = nums1[a_index], nums2[b_index]

            if a_index + b_index < k:
                if a_value > b_value:
                    return solve(k, a_start, a_end, b_index + 1, b_end)
                else:
                    return solve(k, a_index + 1, a_end, b_start, b_end)
            else:
                if a_value > b_value:
                    return solve(k, a_start, a_index - 1, b_start, b_end)
                else:
                    return solve(k, a_start, a_end, b_start, b_index - 1)

        if n % 2:
            return solve(n // 2, 0, na - 1, 0, nb - 1)
        else:
            return (solve(n // 2 - 1, 0, na - 1, 0, nb - 1) + solve(n // 2, 0, na - 1, 0, nb - 1)) / 2
