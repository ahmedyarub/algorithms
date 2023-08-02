class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        sums = defaultdict(int)

        for k, v in nums1:
            sums[k] += v

        for k, v in nums2:
            sums[k] += v

        return sorted([[k, sums[k]] for k in sums.keys()])
