class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(map({num2: i for i, num2 in enumerate(nums2)}.get, nums1))
